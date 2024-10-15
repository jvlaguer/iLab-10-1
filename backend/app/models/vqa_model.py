from transformers import RobertaTokenizer, TFRobertaModel
from tensorflow.keras.applications import ResNet50
import keras
import os
import boto3
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')

# Initialize a session using Amazon S3
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

# Define the S3 bucket and file details
BUCKET_NAME = "roberta-finetuned"
FILE_KEY = "vqa_model_roberta_finetuned.keras"


# Define the VQAModel class with Keras model
class VQAModel:
    def __init__(self, dropbox_url):
        # Set the path for the model file inside the models directory
        model_path = os.path.join(
            os.path.dirname(__file__), "vqa_model_roberta_finetuned.keras"
        )

        # Check if the model file already exists
        if not os.path.exists(model_path):
            self.download_model(model_path)

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

    def download_model(self, model_path):
        # Download the model from S3
        print(f"Downloading model from s3 to {model_path}...")

        # Download the file from S3
        s3.download_file(BUCKET_NAME, FILE_KEY, model_path)
        print("Model downloaded successfully.")
