import React from 'react';
import AuthForm from '../components/AuthForm';

function Signup() {
  return (
    <div className="signup">
      <h1>Signup</h1>
      <AuthForm mode="signup" />
    </div>
  );
}

export default Signup;
