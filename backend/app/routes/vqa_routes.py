from flask import Blueprint, request, jsonify
from app.services.vqa_service import predict_vqa
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

vqa_routes = Blueprint('vqa', __name__)

@vqa_routes.route('/vqa', methods=['POST'])
def vqa():
    # verify whether the vqa endpoint is reached
    logger.info("Test endpoint reached")
    
    image = request.files.get('image')
    question = request.form.get('question')

    # Call the VQA service to get predictions
    answer = predict_vqa(question, image)

    return jsonify({'answer': answer})