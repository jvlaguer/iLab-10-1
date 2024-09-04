from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)
sessions = {}

@app.route('/api/process', methods=['POST'])
def process():
    if 'image' not in request.files or 'question' not in request.form:
        return jsonify({'error': 'Image and question are required'}), 400
    
    image = request.files['image']
    question = request.form['question']

    # Generate a session ID
    session_id = str(uuid.uuid4())

    # Save session data
    sessions[session_id] = {
        'image': image.read(),  
        'question': question,
        'chat_history': []
    }

    return jsonify({
        'message': 'Image and question received successfully',
        'session_id': session_id
    })

@app.route('/api/resume', methods=['POST'])
def resume():
    data = request.json
    session_id = data.get('session_id')

    if session_id not in sessions:
        return jsonify({'error': 'Session ID not found'}), 404

    # Retrieve session data
    session_data = sessions[session_id]

    return jsonify({
        'success': True,
        'image': session_data['image'],
        'question': session_data['question'],
        'chat_history': session_data['chat_history'] 
    })

if __name__ == '__main__':
    app.run(debug=True)
