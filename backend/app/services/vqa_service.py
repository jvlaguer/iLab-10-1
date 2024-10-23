# Services to manage image & questions preprocessing
from backend.app.models.vqa_model import VQAModel
import numpy as np
import tensorflow as tf

tf.config.set_visible_devices([], "GPU")
from torchvision import transforms
import torch
from PIL import Image

# Initialize VQAModel and get necessary models
vqa_model = VQAModel()
model = vqa_model.get_model()
blip_processor = vqa_model.get_processor()
rad_classifier = vqa_model.get_rad_classifier()

def preprocess_image(img):
    transform = transforms.Compose(
        [
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]
            ),  # ImageNet normalization
        ]
    )

    # Open image and convert to RGB
    image = Image.open(img).convert("RGB")

    # Apply transformations
    image = transform(image)

    # Add batch dimension (for a single image)
    image = image.unsqueeze(0)

    return image

def is_radiology_image(image):
    img_processed = preprocess_image(image)
    # Predict on the preprocessed image
    with torch.no_grad():
        classification_output = rad_classifier(img_processed)
        predicted_prob = torch.sigmoid(classification_output).item()
        predicted_class = 1 if predicted_prob > 0.5 else 0
    return predicted_class


# Function to predict the answer
def predict_vqa(question, image):
    # Process the question with BLIP for a descriptive answer
    if is_radiology_image(image):
        image = Image.open(image)
        inputs = blip_processor(image, question, return_tensors="pt")
        outputs = model.generate(
            pixel_values=inputs["pixel_values"], input_ids=inputs["input_ids"]
        )

        # Decode the predicted answer
        answer = blip_processor.decode(outputs[0], skip_special_tokens=True)
        return answer
    else:
        return"The uploaded image doesn’t appear to be a radiology image. Please provide a valid radiology image for better assistance."