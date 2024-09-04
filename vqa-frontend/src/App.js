import React, { useState, useEffect } from 'react';
import { Container, Typography, Box, TextField, Button } from '@mui/material';
import UploadImage from './components/UploadImage';
import TextInput from './components/TextInput';
import SubmitButton from './components/SubmitButton';
import LoadingScreen from './components/LoadingScreen';
import ChatPage from './components/ChatPage';
import axios from 'axios';

function App() {
    const [loading, setLoading] = useState(true);
    const [image, setImage] = useState(null);
    const [question, setQuestion] = useState('');
    const [submitted, setSubmitted] = useState(false);
    const [sessionId, setSessionId] = useState('');
    const [resumeSession, setResumeSession] = useState(false);

    useEffect(() => {
        setTimeout(() => setLoading(false), 2000);
    }, []);

    const handleResumeSession = async () => {
        try {
            const response = await axios.post('/api/resume', { session_id: sessionId });
            if (response.data.success) {
                setSubmitted(true);
                // Optionally, we can pass the previous chat history to ChatPage here
            } else {
                alert('Invalid session ID.');
            }
        } catch (error) {
            console.error('Error resuming session:', error);
        }
    };

    if (loading) {
        return <LoadingScreen />;
    }

    if (submitted || resumeSession) {
        return <ChatPage sessionId={sessionId} />;
    }

    return (
        <Container
            maxWidth="sm"
            style={{
                height: '100vh',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'center',
                alignItems: 'center',
                textAlign: 'center',
            }}
        >
            <Box>
                <Typography variant="h4" gutterBottom>
                    MedVisor
                </Typography>
                <Typography variant="body1" gutterBottom>
                    Welcome! Please upload a medical image and enter your question below to begin a Visual Question Answering session.
                </Typography>
                <UploadImage setImage={setImage} />
                <TextInput setQuestion={setQuestion} />
                <SubmitButton
                    image={image}
                    question={question}
                    setSubmitted={setSubmitted}
                    setSessionId={setSessionId}
                />
                <Typography variant="body2" style={{ marginTop: '20px' }}>
                    Or resume a previous session:
                </Typography>
                <TextField
                    label="Session ID"
                    variant="outlined"
                    fullWidth
                    value={sessionId}
                    onChange={(e) => setSessionId(e.target.value)}
                    style={{ marginTop: '10px' }}
                />
                <Button
                    variant="contained"
                    color="primary"
                    onClick={handleResumeSession}
                    style={{ marginTop: '10px' }}
                >
                    Resume Session
                </Button>
            </Box>
        </Container>
    );
}

export default App;
