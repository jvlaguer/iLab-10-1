import os
import boto3
from dotenv import load_dotenv
from transformers import BlipProcessor, BlipForQuestionAnswering

# Load environment variables from the .env file
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

# Initialize a session using Amazon S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION,
)

# Define the S3 bucket and folder details
BUCKET_NAME = "roberta-finetuned"
FOLDER_KEY = "blip_finetuned_model/"  # S3 folder path


# Define the VQAModel class with Keras model
class VQAModel:
    def __init__(self):
        # Set the path for the model folder inside the models directory
        self.model_path = os.path.join(os.path.dirname(__file__), "blip_finetuned_model")

        # Check if the model folder already exists
        if not os.path.exists(self.model_path):
            self.download_model()

        # Load the pre-trained model and processor
        self.model = BlipForQuestionAnswering.from_pretrained(self.model_path)
        self.processor = BlipProcessor.from_pretrained(self.model_path)

    def get_model(self):
        return self.model

    def get_processor(self):
        return self.processor

    def download_model(self):
        # Ensure the local directory exists
        if not os.path.exists(self.model_path):
            os.makedirs(self.model_path)

        # List all objects in the folder
        paginator = s3.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=BUCKET_NAME, Prefix=FOLDER_KEY):
            if 'Contents' in page:
                for obj in page['Contents']:
                    # Get the file key (S3 path of the file)
                    file_key = obj['Key']

                    # Construct the local path by removing the S3 folder prefix from the file key
                    local_file_path = os.path.join(self.model_path, file_key[len(FOLDER_KEY):])

                    # Download the file from S3
                    print(f"Downloading {file_key} to {local_file_path}...")
                    s3.download_file(BUCKET_NAME, file_key, local_file_path)

        print("Model folder downloaded successfully.")