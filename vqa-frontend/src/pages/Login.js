import React from 'react';
import AuthForm from '../components/AuthForm';

function Login() {
  return (
    <div className="login">
      <h1>Login</h1>
      <AuthForm mode="login" />
    </div>
  );
}

export default Login;
