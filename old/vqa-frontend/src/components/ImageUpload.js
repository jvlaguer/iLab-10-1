import React, { useState } from 'react';
import './ImageUpload.css'; // Add custom styles

function ImageUpload() {
  const [image, setImage] = useState(null);
  const [text, setText] = useState('');

  const handleImageChange = (e) => {
    setImage(URL.createObjectURL(e.target.files[0]));
  };

  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  return (
    <div className="image-upload">
      <input type="file" accept="image/*" onChange={handleImageChange} />
      <textarea
        value={text}
        onChange={handleTextChange}
        maxLength={300}
        placeholder="Enter your question (max 300 characters)"
      />
      {image && (
        <div className="image-preview">
          <img src={image} alt="Preview" />
        </div>
      )}
    </div>
  );
}

export default ImageUpload;
