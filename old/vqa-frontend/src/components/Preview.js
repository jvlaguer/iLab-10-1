import React from 'react';
import './Preview.css'; // Add custom styles

function Preview({ image, text }) {
  return (
    <div className="preview">
      {image && <img src={image} alt="Preview" />}
      <p>{text}</p>
    </div>
  );
}

export default Preview;