from flask import Flask, request, jsonify
from flask_cors import CORS
from predict import predict_disease_class
from lib.gemini import generate_disease_info
from lib.save import log_prediction


app = Flask(__name__)

CORS(app)


@app.route('/')
def home():
    return "Hello YEZA!"


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        try:
            predicted_class_name, confidence_score = predict_disease_class(file)
            best_practice= generate_disease_info(predicted_class_name)

            log_prediction(file, predicted_class_name, confidence_score)

            return jsonify({
                'predicted_class': predicted_class_name,
                'confidence': f"{confidence_score:.2f}%",
                'best practice': best_practice
            })
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Failed to load model!"}), 500




if __name__ == '__main__':
    app.run()