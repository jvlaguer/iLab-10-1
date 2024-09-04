import React from 'react';
import { CircularProgress, Box, Typography } from '@mui/material';

function LoadingScreen() {
  return (
    <Box
      style={{
        height: '100vh',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',
        flexDirection: 'column',
      }}
    >
      <CircularProgress />
      <Typography variant="h6" style={{ marginTop: '20px' }}>
        Loading...
      </Typography>
    </Box>
  );
}

export default LoadingScreen;
