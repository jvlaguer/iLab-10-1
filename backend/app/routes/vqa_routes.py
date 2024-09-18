from flask import Blueprint, request, jsonify
from backend.app.services.vqa_service import process_vqa

vqa_routes = Blueprint('vqa', __name__)

@vqa_routes.route('/vqa', methods=['POST'])
def vqa():
    image = request.files.get('image')
    question = request.form.get('question')

    # Call the VQA service to get predictions
    answer = process_vqa(image, question)

    return jsonify({'answer': answer})