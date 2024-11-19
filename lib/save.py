import os, json
from datetime import datetime


def log_prediction(file, predicted_class_name, confidence_score, model_name="ModelName"):
    date_folder = datetime.now().strftime("%Y-%m-%d")
    base_folder = "Predictions/Input_Images"
    folder_path = os.path.join(base_folder, date_folder)
    os.makedirs(folder_path, exist_ok=True)

    unique_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
    image_filename = f"{unique_id}.jpg"
    image_path = os.path.join(folder_path, image_filename)
    file.save(image_path)

    log_data = {
        "image_id": unique_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "predicted_class": predicted_class_name,
        "model_name": model_name,
        "confidence": f"{confidence_score:.2f}%"
    }

    log_filename = "predictions_log.json"
    log_path = os.path.join('Predictions', log_filename)

    if os.path.exists(log_path):
        with open(log_path, 'r+') as log_file:
            data = json.load(log_file)
            data["predictions"].append(log_data)
            log_file.seek(0)
            json.dump(data, log_file, indent=4)
    else:
        with open(log_path, 'w') as log_file:
            json.dump({"predictions": [log_data]}, log_file, indent=4)

    return image_path
