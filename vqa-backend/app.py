from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from utils.image_processing import preprocess_image
from utils.question_processing import preprocess_question
from utils.model_inference import get_answer
from database import init_db, save_interaction

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

# Initialize database connection
init_db()

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        processed_image = preprocess_image(filepath)
        return jsonify({'message': 'Image uploaded and processed successfully', 'image_path': filepath}), 200

@app.route('/ask_question', methods=['POST'])
def ask_question():
    data = request.json
    if 'image_path' not in data or 'question' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    image_path = data['image_path']
    question = data['question']
    
    processed_image = preprocess_image(image_path)
    processed_question = preprocess_question(question)
    
    # Get the answer from the ML model
    answer = get_answer(processed_image, processed_question)
    
    # Save interaction in the database
    save_interaction(image_path, question, answer)
    
    return jsonify({'question': question, 'answer': answer}), 200

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
