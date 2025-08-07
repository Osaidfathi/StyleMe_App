from flask import Blueprint, request, jsonify
import os
import base64
import numpy as np
import cv2
import logging

ai_bp = Blueprint('ai_bp', __name__)

# Initialize AI models with error handling
try:
    from deepface import DeepFace
    deepface_available = True
    logging.info("DeepFace loaded successfully")
except ImportError as e:
    deepface_available = False
    logging.error(f"Error importing DeepFace: {e}")

# Try to import HairCLIP or alternative hair styling model
try:
    # This would be the actual HairCLIP import if available
    # from hairclip import HairCLIP
    # hair_model = HairCLIP()
    hair_model_available = False
    logging.info("Hair styling model not available - using placeholder")
except ImportError as e:
    hair_model_available = False
    logging.error(f"Error importing HairCLIP: {e}")

# Fallback to basic image processing if AI models are not available
def create_mock_hairstyle_change(image):
    """Create a mock hairstyle change for demonstration purposes"""
    # This is a placeholder that just applies a simple filter
    # In a real implementation, this would use proper AI models
    from PIL import Image, ImageEnhance
    
    # Convert to PIL Image
    pil_img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    # Apply some basic enhancement to simulate a "change"
    enhancer = ImageEnhance.Brightness(pil_img)
    enhanced_img = enhancer.enhance(1.1)
    
    enhancer = ImageEnhance.Contrast(enhanced_img)
    final_img = enhancer.enhance(1.05)
    
    return final_img

@ai_bp.route('/analyze_face', methods=['POST'])
def analyze_face():
    try:
        data = request.json
        if 'image' not in data:
            return jsonify({'error': 'No image provided'}), 400

        if not deepface_available:
            # Return mock analysis if DeepFace is not available
            return jsonify({
                'analysis': {
                    'age': 25,
                    'gender': {'Woman': 45.2, 'Man': 54.8},
                    'race': {'asian': 20, 'indian': 10, 'black': 15, 'white': 45, 'middle eastern': 5, 'latino hispanic': 5},
                    'emotion': {'angry': 5, 'disgust': 2, 'fear': 3, 'happy': 70, 'sad': 5, 'surprise': 10, 'neutral': 5}
                },
                'note': 'Using mock data - DeepFace not available'
            }), 200

        image_data = data['image']
        # Decode base64 image
        img_bytes = base64.b64decode(image_data.split(',')[1])
        np_arr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Save image temporarily for DeepFace (DeepFace expects file path)
        temp_img_path = 'temp_face_image.jpg'
        cv2.imwrite(temp_img_path, img)

        try:
            # Perform facial analysis using DeepFace
            demography = DeepFace.analyze(img_path=temp_img_path, actions=['age', 'gender', 'race', 'emotion'], enforce_detection=False)
            
            # Clean up temporary file
            if os.path.exists(temp_img_path):
                os.remove(temp_img_path)

            return jsonify({'analysis': demography}), 200
        except Exception as deepface_error:
            # Clean up temporary file even if DeepFace fails
            if os.path.exists(temp_img_path):
                os.remove(temp_img_path)
            
            # Return mock data if DeepFace analysis fails
            return jsonify({
                'analysis': {
                    'age': 25,
                    'gender': {'Woman': 45.2, 'Man': 54.8},
                    'race': {'asian': 20, 'indian': 10, 'black': 15, 'white': 45, 'middle eastern': 5, 'latino hispanic': 5},
                    'emotion': {'angry': 5, 'disgust': 2, 'fear': 3, 'happy': 70, 'sad': 5, 'surprise': 10, 'neutral': 5}
                },
                'note': f'Using mock data - DeepFace analysis failed: {str(deepface_error)}'
            }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ai_bp.route('/generate_hairstyle', methods=['POST'])
def generate_hairstyle():
    try:
        data = request.json
        if 'image' not in data or 'prompt' not in data:
            return jsonify({'error': 'Image and prompt are required'}), 400

        image_data = data['image']
        prompt = data['prompt']

        # Decode base64 image
        img_bytes = base64.b64decode(image_data.split(',')[1])
        np_arr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Use mock hairstyle generation since HairCLIP is not available
        generated_image = create_mock_hairstyle_change(img)

        # Encode generated image back to base64
        import io
        buffered = io.BytesIO()
        generated_image.save(buffered, format="PNG")
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')

        return jsonify({
            'generated_image': f'data:image/png;base64,{encoded_image}',
            'note': 'Using mock hairstyle generation - AI model not available',
            'prompt_used': prompt
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ai_bp.route('/modify_hairstyle', methods=['POST'])
def modify_hairstyle():
    try:
        data = request.json
        if 'image' not in data or 'modification_prompt' not in data:
            return jsonify({'error': 'Image and modification_prompt are required'}), 400

        image_data = data['image']
        modification_prompt = data['modification_prompt']

        # Decode base64 image
        img_bytes = base64.b64decode(image_data.split(',')[1])
        np_arr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Use mock hairstyle modification since HairCLIP is not available
        modified_image = create_mock_hairstyle_change(img)

        # Encode modified image back to base64
        import io
        buffered = io.BytesIO()
        modified_image.save(buffered, format="PNG")
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')

        return jsonify({
            'modified_image': f'data:image/png;base64,{encoded_image}',
            'note': 'Using mock hairstyle modification - AI model not available',
            'modification_used': modification_prompt
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Add a health check endpoint for AI services
@ai_bp.route('/health', methods=['GET'])
def ai_health():
    return jsonify({
        'status': 'ok',
        'deepface_available': deepface_available,
        'hair_model_available': hair_model_available,
        'message': 'AI services are running with fallback implementations'
    }), 200


