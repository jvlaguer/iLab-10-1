from backend.app.models.vqa_model import get_model, get_tokenizer
from PIL import Image
import numpy as np
import os

# Get the directory of the current file (vqa_service.py)
current_directory = os.path.dirname(__file__)

# Build the relative path to the model
model_path = os.path.join(current_directory, '../models/vqa_model_roberta.h5')

# Load model and tokenizer
vqa_model = get_model(model_path=model_path)
tokenizer = get_tokenizer(tokenizer_path='roberta-base')

def process_vqa(image_file, question):
    # Load and process the image
    image = Image.open(image_file).convert('RGB')
    image = image.resize((224, 224))  # Adjust size based on model input
    img_array = np.array(image) / 255.0  # Normalize image

    # Tokenize the question
    inputs = tokenizer(question, return_tensors="tf")

    # Run the model prediction
    predictions = vqa_model.predict([np.expand_dims(img_array, axis=0), inputs['input_ids']])

    # Convert predictions to human-readable answer
    predicted_answer = np.argmax(predictions, axis=-1)
    return str(predicted_answer)