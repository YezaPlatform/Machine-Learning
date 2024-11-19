import json
import keras
from PIL import Image
import numpy as np
import os
from dotenv import load_dotenv


load_dotenv()


model_path=os.getenv("MODEL_PATH")


MODEL_NAME = model_path

try:
    model = keras.models.load_model(MODEL_NAME)
except ValueError as e:
    print(f"Error loading model: {e}")


with open('class_indices.json', 'r') as file:
    class_indices = json.load(file)



def preprocess_image(image_path, target_size=(256, 256)):
    img = Image.open(image_path)
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.
    return img_array



def predict_disease_class(image_file):
    preprocessed_img = preprocess_image(image_file)
    predictions = model.predict(preprocessed_img)
    
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)]

    confidence_score = predictions[0][predicted_class_index] * 100
    return predicted_class_name, confidence_score