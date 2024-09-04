import React from 'react';
import { Input, Box } from '@mui/material';

function UploadImage({ setImage }) {
  const handleFileChange = (event) => {
    if (event.target.files.length > 0) {
      setImage(event.target.files[0]);
    }
  };

  return (
    <Box style={{ textAlign: 'center', marginBottom: '1rem' }}>
      <Input
        type="file"
        onChange={handleFileChange}
        inputProps={{ accept: 'image/*' }}
        fullWidth
      />
    </Box>
  );
}

export default UploadImage;
