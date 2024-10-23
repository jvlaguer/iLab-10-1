# Services to manage image & questions preprocessing
from backend.app.models.vqa_model import VQAModel
import numpy as np
import tensorflow as tf
tf.config.set_visible_devices([], "GPU")

from PIL import Image

# Initialize VQAModel and get necessary models
vqa_model = VQAModel()
model = vqa_model.get_model()
blip_processor = vqa_model.get_processor()

def preprocess_image(img):
    img = Image.open(img)
    # Convert to PIL Image if not already
    if not isinstance(img, Image.Image):
        img = Image.fromarray(img)
    # Check the size of the image
    width, height = img.size
    # Convert the image to RGB if necessary
    if img.mode != 'RGB':
        img = img.convert('RGB')
    # Resize image to (224, 224) for model input
    img = img.resize((224, 224))
    return img

# Function to predict the answer
def predict_vqa(question, image):
    # Process the question with BLIP for a descriptive answer
    image = Image.open(image)
    inputs = blip_processor(image, question, return_tensors="pt")
    outputs = model.generate(pixel_values=inputs['pixel_values'],
                          input_ids=inputs['input_ids'])

    # Decode the predicted answer
    answer = blip_processor.decode(outputs[0], skip_special_tokens=True)
    return answer