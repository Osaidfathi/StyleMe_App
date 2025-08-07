import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS # Import CORS
from src.models.user import db
from src.routes.user import user_bp
from src.routes.ai_routes import ai_bp # Import AI blueprint
from src.routes.booking_routes import booking_bp # Import Booking blueprint
from src.routes.salon_dashboard import salon_dashboard_bp # Import Salon Dashboard blueprint
from src.routes.admin_dashboard import admin_dashboard_bp # Import Admin Dashboard blueprint
from src.routes.admin_ui_routes import admin_ui_bp # Import Admin UI blueprint
app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# استخدم os.environ.get لقراءة متغيرات البيئة من Vercel
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

CORS(app) # Enable CORS for all routes

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(ai_bp, url_prefix='/api/ai') # Register AI blueprint
app.register_blueprint(booking_bp, url_prefix='/api/booking') # Register Booking blueprint
app.register_blueprint(salon_dashboard_bp, url_prefix='/api/salon') # Register Salon Dashboard blueprint
app.register_blueprint(admin_dashboard_bp, url_prefix="/api/admin") # Register Admin Dashboard blueprint
app.register_blueprint(admin_ui_bp) # Register Admin UI blueprint

# استخدم os.environ.get لقراءة رابط قاعدة البيانات من Vercel
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
