# Crop Need Recognition Model - Agrio Clone Mobile Application

## Project Overview
This project is part of the Agrio Clone Mobile Application, where the goal is to develop an AI-powered solution for recognizing crop needs (such as water, nutrients, or pest control) based on image features. The model will help farmers by analyzing crop images and providing actionable recommendations to improve crop health.

## Machine Learning Stack
For the development of this machine learning model, the following tools and libraries are used:

### 1. **TensorFlow and Keras**
- **TensorFlow** is an open-source platform for machine learning. It's used to build, train, and deploy deep learning models.
- **Keras**, which runs on top of TensorFlow, is used for easy and efficient model building, especially for image classification tasks.
  
### 2. **OpenCV**
- **OpenCV** is a powerful computer vision library. It is used here for image preprocessing, including tasks like resizing, normalization, and feature extraction from the input images.

### 3. **Scikit-learn**
- **Scikit-learn** is a machine learning library that provides various tools for model development, feature extraction, and classification. It complements TensorFlow by handling preprocessing and some feature extraction tasks.

### 4. **Flask**
- **Flask** is a micro web framework used to create the RESTful API that will serve the ML model. It enables easy integration of the trained model into a web interface for interacting with the mobile application.

### 5. **Pillow (PIL)**
- **Pillow** is a Python Imaging Library that will be used for handling image input and converting them into formats suitable for processing by OpenCV and TensorFlow.

## Installation
To set up the project, clone the repository and install the dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
