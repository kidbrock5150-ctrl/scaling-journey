
# CashCatch AI Backend (Render-Ready)

This is a simple Python Flask server designed to:
1. Accept image uploads from the CashCatch Glide app.
2. Detect U.S. coin and currency errors using a pre-trained TensorFlow Lite model.
3. Estimate potential value based on known data or via eBay API integration (optional).

## Deployment on Render

1. Go to https://render.com and create a new Web Service
2. Upload this code as a .zip or connect to a GitHub repo
3. Set the build command: pip install -r requirements.txt
4. Set the start command: python app.py
5. Service must run on port 5000 (Render default)

## Endpoints

- POST /analyze
  - Form-data key: image (file)
  - Returns: JSON with error type, confidence, estimated value
