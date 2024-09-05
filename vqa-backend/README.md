# VQA Backend

## Description
This folder contains the backend logic for the Visual Question Answering (VQA) system. The backend is built using Python and Flask, and it connects to a PostgreSQL database to store and manage data.

## Project Structure
- `app.py`: Main Flask application. Handles API requests from the frontend, processes image and question data, and returns results.
- `config.py`: Contains configuration settings for the PostgreSQL database connection.
- `database.py`: Manages interactions with the PostgreSQL database. This file includes connection setup, models, and database querying functions.
- `models/`: Directory containing trained machine learning models (e.g., saved model files for the VQA system).
- `utils/`: Helper functions for preprocessing images and questions, and for interacting with the ML model.
  - `image_processing.py`: Functions to preprocess radiology images.
  - `question_processing.py`: Functions to preprocess and tokenize text questions.
  - `model_inference.py`: Code for running inference on the ML model to generate answers.

## Setup Instructions
1. Install dependencies using `pip`:
2. Configure the database in `config.py` with the correct PostgreSQL settings.
3. Run the Flask server:
4. The server will run on `http://localhost:5000/`.

## API Endpoints
- **POST /upload_image**: Uploads an image and returns a processed version.
- **POST /ask_question**: Submits a question related to an image and returns an answer.
