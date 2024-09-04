import React, { useState, useEffect } from 'react';
import { Box, TextField, Button, Typography, Paper } from '@mui/material';
import { useLocation } from 'react-router-dom';

function ChatPage() {
  const location = useLocation();
  const image = location.state?.image;
  const sessionId = location.state?.sessionId;
  const initialChatHistory = location.state?.chatHistory || [];

  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState(initialChatHistory);

  useEffect(() => {
    if (sessionId) {
      console.log(`Connected to session: ${sessionId}`);
    }
  }, [sessionId]);

  const handleSendMessage = () => {
    if (message.trim()) {
      const newChatHistory = [
        ...chatHistory,
        { text: message, sender: 'user' },
        { text: 'This is a simulated response.', sender: 'bot' },
      ];
      setChatHistory(newChatHistory);
      setMessage('');
    }
  };

  return (
    <Box style={{ padding: '20px', maxWidth: '800px', margin: 'auto' }}>
      <Typography variant="h4" gutterBottom>
        Chat about the Image
      </Typography>

      {/* Display the uploaded image */}
      {image && (
        <Box style={{ textAlign: 'center', marginBottom: '20px' }}>
          <img
            src={URL.createObjectURL(image)}
            alt="Uploaded"
            style={{ maxWidth: '100%', maxHeight: '300px', borderRadius: '10px' }}
          />
        </Box>
      )}

      {/* Chat history */}
      <Paper style={{ padding: '20px', maxHeight: '400px', overflowY: 'auto' }}>
        {chatHistory.map((chat, index) => (
          <Box key={index} style={{ marginBottom: '10px', textAlign: chat.sender === 'user' ? 'right' : 'left' }}>
            <Typography
              variant="body1"
              style={{
                backgroundColor: chat.sender === 'user' ? '#d1eaff' : '#f1f1f1',
                padding: '10px',
                borderRadius: '10px',
                display: 'inline-block',
              }}
            >
              {chat.text}
            </Typography>
          </Box>
        ))}
      </Paper>

      {/* Input and Send button */}
      <Box style={{ display: 'flex', marginTop: '20px' }}>
        <TextField
          variant="outlined"
          fullWidth
          placeholder="Type your message..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <Button
          variant="contained"
          color="primary"
          onClick={handleSendMessage}
          style={{ marginLeft: '10px' }}
        >
          Send
        </Button>
      </Box>
    </Box>
  );
}

export default ChatPage;
