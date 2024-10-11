import tensorflow as tf
from transformers import RobertaTokenizer, TFRobertaModel
from tensorflow.keras.applications import ResNet50
import keras
import os
import requests


# Define the VQAModel class with Keras model
class VQAModel:
    def __init__(self, dropbox_url):

        # Set the path for the model file inside the models directory
        model_path = os.path.join(os.path.dirname(__file__), "vqa_model_roberta_finetuned.keras")

        # Check if the model file already exists
        if not os.path.exists(model_path):
            self.download_model(dropbox_url, model_path)

        # Load the pre-trained Keras model
        self.model = keras.models.load_model(model_path)

        # Initialize ResNet50 model for image feature extraction
        self.resnet_model = ResNet50(
            weights="imagenet", include_top=False, input_shape=(224, 224, 3)
        )

        # Load the pre-trained Roberta Tokenizer and model
        self.tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
        self.roberta_model = TFRobertaModel.from_pretrained("roberta-large")

    def get_model(self):
        return self.model

    def get_resnet(self):
        return self.resnet_model

    def get_tokenizer(self):
        return self.tokenizer

    def get_roberta_model(self):
        return self.roberta_model

    def download_model(self, url, model_path):
        # Download the model from Dropbox
        print(f"Downloading model from {url} to {model_path}...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(model_path, "wb") as f:
                f.write(response.content)
            print(f"Model downloaded and saved to {model_path}.")
        else:
            raise Exception("Failed to download the model from Dropbox.")
