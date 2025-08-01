
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load model (placeholder)
# model = tf.lite.Interpreter(model_path="coin_model.tflite")
# model.allocate_tensors()

@app.route('/')
def home():
    return "CashCatch AI Backend is running."

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image = Image.open(image_file.stream).convert('RGB')
    image = image.resize((224, 224))
    image_np = np.array(image) / 255.0
    image_np = np.expand_dims(image_np, axis=0)

    # Fake prediction output
    response = {
        "error_type": "Double Die Reverse",
        "confidence": 0.87,
        "estimated_value": "$150 - $300"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
