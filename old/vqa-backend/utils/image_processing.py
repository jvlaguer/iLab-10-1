from PIL import Image
import numpy as np

def preprocess_image(image_path):
    """
    Preprocesses the image by converting it to grayscale, resizing, and normalizing.
    :param image_path: Path to the image file
    :return: Preprocessed image array
    """
    image = Image.open(image_path)
    image = image.convert('L')  # Convert to grayscale
    image = image.resize((224, 224))  # Resize to (224, 224)
    image_array = np.array(image) / 255.0  # Normalize pixel values
    return image_array
