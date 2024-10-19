import torch
from transformers import RobertaModel

# Load pre-trained RoBERTa model
model = RobertaModel.from_pretrained('roberta-base')

def get_answer(image, question):
    """
    Generates an answer by fusing image and question features and running inference through the model.
    :param image: Preprocessed image array
    :param question: Preprocessed question tokens
    :return: Predicted answer as a string
    """
    # Image and question features can be fused and passed into a final model
    image_features = torch.tensor(image).unsqueeze(0)  # Add batch dimension
    question_features = model(**question).last_hidden_state
    
    # For demonstration purposes, we'll return a dummy answer
    return "dummy answer"  # Placeholder: Replace with actual model inference logic
