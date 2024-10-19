// src/components/Navbar.js
import React, { useState } from 'react';
import './Navbar.css';
import { Link } from 'react-router-dom';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleNavbar = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <h1 className="navbar-logo">MedVisor</h1>
        <div className="menu-icon" onClick={toggleNavbar}>
          <i className={isOpen ? 'fas fa-times' : 'fas fa-bars'}></i>
        </div>
        <ul className={`nav-menu ${isOpen ? 'active' : ''}`}>
          <li className="nav-item">
            <Link to="/" className="nav-links" onClick={toggleNavbar}>Home</Link>
          </li>
          <li className="nav-item">
            <Link to="/upload" className="nav-links" onClick={toggleNavbar}>Upload</Link>
          </li>
          <li className="nav-item">
            <Link to="/login" className="nav-links" onClick={toggleNavbar}>Login</Link>
          </li>
          <li className="nav-item">
            <Link to="/signup" className="nav-links" onClick={toggleNavbar}>Sign Up</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
