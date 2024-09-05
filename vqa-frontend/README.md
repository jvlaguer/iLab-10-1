# VQA Frontend

## Description
This folder contains the frontend code for the Visual Question Answering (VQA) system. The frontend is built using React.js and Material-UI to create a user interface that interacts with the Flask backend.

## Project Structure
- `src/`: Contains the main React components and views.
  - `App.js`: The main application component that routes between different views.
  - `components/`: React components for uploading images, entering questions, and displaying results.
    - `ImageUpload.js`: Component for uploading images.
    - `QuestionForm.js`: Component for submitting questions.
    - `AnswerDisplay.js`: Component for displaying the generated answers.
  - `api.js`: Axios setup for interacting with the backend API.
  - `styles/`: Custom styles and theme settings.
- `public/`: Contains static files like the index.html.

## Setup Instructions
1. Install dependencies using `npm` or `yarn`:
2. Run the development server
3. The application will run on `http://localhost:3000/`.

## Key Features
- **Image Upload**: Users can upload radiology images.
- **Question Submission**: Users can ask medical-related questions about the uploaded image.
- **Answer Display**: The system returns answers based on the image and question provided.
