import React from 'react';
import { Button, Box } from '@mui/material';
import axios from 'axios';

function SubmitButton({ image, question, setSubmitted }) {
  const handleSubmit = async () => {
    if (!question && !image) {
      alert('Please upload an image or enter a question.');
      return;
    }
    if (image && !question) {
      alert('If you upload an image, you must also enter a question.');
      return;
    }

    try {
      const formData = new FormData();
      if (image) {
        formData.append('file', image);
      }
      if (question) {
        formData.append('question', question);
      }

      const response = await axios.post('http://localhost:5000/api/process', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      alert('Submission successful: ' + response.data.message);
      setSubmitted(true);
    } catch (error) {
      console.error('There was an error sending the data.', error);
      alert('There was an error sending the data.');
    }
  };

  return (
    <Box style={{ textAlign: 'center' }}>
      <Button
        variant="contained"
        color="secondary"
        onClick={handleSubmit}
        fullWidth
      >
        Submit
      </Button>
    </Box>
  );
}

export default SubmitButton;
