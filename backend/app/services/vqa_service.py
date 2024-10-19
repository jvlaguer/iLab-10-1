# Services to manage image & questions preprocessing
from backend.app.models.vqa_model import VQAModel
import numpy as np
import tensorflow as tf
tf.config.set_visible_devices([], 'GPU')
from PIL import Image

# Initialize VQAModel and get necessary models
vqa_model = VQAModel()
model = vqa_model.get_model()
resnet_model = vqa_model.get_resnet()
tokenizer = vqa_model.get_tokenizer()
roberta_model = vqa_model.get_roberta_model()


def preprocess_image(img):
    img = tf.image.resize(img, (224, 224))
    img = tf.image.random_flip_left_right(img)
    img = tf.image.random_brightness(img, 0.2)
    img = np.expand_dims(img, axis=0)
    return img


def process_image_text(image, question):
    # Process image
    img_array = preprocess_image(image)
    img_features = resnet_model.predict(img_array)
    img_features = img_features.reshape((img_features.shape[0], -1))

    # Process question
    inputs = tokenizer.encode_plus(
        question, max_length=512, return_attention_mask=True, return_tensors="tf"
    )
    text_embeddings = roberta_model(
        inputs["input_ids"], attention_mask=inputs["attention_mask"]
    ).last_hidden_state[:, 0, :]

    # Combine features
    combined_features = tf.concat([img_features, text_embeddings], axis=1)
    return combined_features


# Function to predict the answer
def predict_vqa(question, image_file=None):
    # Load image from image_file and convert to RGB
    image = Image.open(image_file).convert("RGB")

    # Process the input (image + question)
    features = process_image_text(image, question)

        # Make predictions using the model
    predictions = model.predict(features)
    
    # Get the predicted answer (yes/no binary classification)
    predicted_class = np.argmax(predictions, axis=1)
    return 'yes' if predicted_class == 1 else 'no'
