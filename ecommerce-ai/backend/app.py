from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import io
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize the model at startup
logger.info("Loading ResNet50 model...")
try:
    model = tf.keras.applications.ResNet50(weights='imagenet')
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    model = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(image_path):
    logger.info(f"Processing image: {image_path}")
    try:
        # Load and preprocess the image
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        img_array = tf.keras.applications.resnet50.preprocess_input(img_array)
        
        # Make prediction
        predictions = model.predict(img_array)
        
        # Get top 5 predictions
        decoded_predictions = tf.keras.applications.resnet50.decode_predictions(predictions, top=5)[0]
        
        # Format predictions
        formatted_predictions = [
            {'category': label, 'confidence': float(score)}
            for (_, label, score) in decoded_predictions
        ]
        
        logger.info(f"Predictions: {formatted_predictions}")
        return formatted_predictions
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        raise

@app.route('/api/analyze', methods=['POST'])
def analyze_product():
    logger.info("Received analyze request")
    if 'file' not in request.files:
        logger.error("No file in request")
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        logger.error("Empty filename")
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        logger.error(f"Invalid file type: {file.filename}")
        return jsonify({'error': 'Invalid file type. Please upload JPG or PNG images'}), 400

    try:
        # Create upload folder if it doesn't exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        # Save the file
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{file.filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        logger.info(f"Saving file to: {filepath}")
        file.save(filepath)

        # Process the image
        if model is None:
            return jsonify({'error': 'Model not initialized'}), 500
            
        predictions = process_image(filepath)
        
        return jsonify({
            'success': True,
            'predictions': predictions,
            'image_url': f'/uploads/{filename}'
        })
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/')
def health_check():
    return jsonify({'status': 'healthy', 'model_loaded': model is not None})

if __name__ == '__main__':
    # Ensure the upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000) 