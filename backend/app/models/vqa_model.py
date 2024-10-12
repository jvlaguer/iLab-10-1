import tensorflow as tf
from transformers import RobertaTokenizer, TFRobertaModel
from tensorflow.keras.applications import ResNet50
import keras

# Define the VQAModel class with Keras model
class VQAModel:
    def __init__(self, model_path):
        # Load the pre-trained Keras model
        self.model = keras.models.load_model(model_path)
        
        # Initialize ResNet50 model for image feature extraction
        self.resnet_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

        # Load the pre-trained Roberta Tokenizer and model
        self.tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
        self.roberta_model = TFRobertaModel.from_pretrained('roberta-large')

    def get_model(self):
        return self.model
    
    def get_resnet(self):
        return self.resnet_model

    def get_tokenizer(self):
        return self.tokenizer
    
    def get_roberta_model(self):
        return self.roberta_model