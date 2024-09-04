import React from 'react';
import { TextField, Box } from '@mui/material';

function TextInput({ setQuestion }) {
  const handleChange = (event) => {
    setQuestion(event.target.value);
  };

  return (
    <Box style={{ textAlign: 'center', marginBottom: '1rem' }}>
      <TextField
        label="Enter your question"
        variant="outlined"
        onChange={handleChange}
        fullWidth
        multiline
        rows={4}
        inputProps={{ maxLength: 300 }}
        helperText="Max 300 characters"
      />
    </Box>
  );
}

export default TextInput;
