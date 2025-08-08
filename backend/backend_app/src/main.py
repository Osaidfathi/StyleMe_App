# File: backend/backend_app/src/main.py
import os
import sys
from pathlib import Path

# Allow imports from package root (adjust path as needed)
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from flask_compress import Compress
from src.models.user import db
from src.routes.user import user_bp
from src.routes.ai_routes import ai_bp
from src.routes.booking_routes import booking_bp
from src.routes.salon_dashboard import salon_dashboard_bp
from src.routes.admin_dashboard import admin_dashboard_bp
from src.routes.admin_ui_routes import admin_ui_bp

# Create Flask app. Do NOT set static_folder here to the SPA's dist — Vercel serves static build separately.
app = Flask(__name__, static_folder=None)

# Enable CORS for /api/* endpoints only
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Enable gzip compression for responses
Compress(app)

# ---------- Configuration ----------
# Prefer DATABASE_URL (or DATABASE) env var (set this on Vercel Dashboard).
# Fallback to a local sqlite file for local dev only.
db_url = os.environ.get("DATABASE_URL") or os.environ.get("DATABASE") 
if not db_url:
    db_dir = Path(os.path.dirname(__file__)) / "database"
    db_dir.mkdir(parents=True, exist_ok=True)
    local_db = db_dir / "app.db"
    db_url = f"sqlite:///{local_db}"

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configure debug from env (default False in production)
app.debug = os.environ.get("FLASK_DEBUG", "0") == "1"

# Initialize DB
db.init_app(app)
with app.app_context():
    db.create_all()

# ---------- Register blueprints under /api/ prefix ----------
# Ensure your blueprints expect to be under /api/...
app.register_blueprint(user_bp, url_prefix="/api/user")
app.register_blueprint(ai_bp, url_prefix="/api/ai")
app.register_blueprint(booking_bp, url_prefix="/api/booking")
app.register_blueprint(salon_dashboard_bp, url_prefix="/api/salon")
app.register_blueprint(admin_dashboard_bp, url_prefix="/api/admin")
# Admin UI blueprint already serves static admin UI; keep default path if desired
app.register_blueprint(admin_ui_bp)

# ---------- Healthcheck and error handlers ----------
@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "env": os.environ.get("FLASK_ENV", "production")})

@app.errorhandler(404)
def not_found(e):
    # For unknown API routes: return JSON (avoid HTML 404 which confuses API clients)
    if (str(e) is not None) and ("/api/" in getattr(e, "description", "") or "/api/" in getattr(e, "name", "")):
        return jsonify({"error": "Not Found"}), 404
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal Server Error"}), 500

# ---------- (Optional) Serve static files for admin UI from backend if needed locally ----------
# If you want to serve some static files from backend (local dev) uncomment and adjust path:
# @app.route("/admin_panel/<path:filename>")
# def serve_admin_static(filename):
#     admin_static = os.path.join(os.path.dirname(__file__), "routes", "static")
#     return send_from_directory(admin_static, filename)

# WSGI/ASGI entrypoint for Vercel / other hosts: expose 'app'
if __name__ == "__main__":
    # For local testing only:
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=app.debug)
