import React, { useState } from "react";
import axios from "axios";
import ChatBubble from "./ChatBubble";

function Chatbot() {
  const [messages, setMessages] = useState([]);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    // Add user bubble
    setMessages((prev) => [...prev, { sender: "user", content: `Uploaded: ${file.name}` }]);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:8000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      // Add bot bubble with JSON response
      setMessages((prev) => [...prev, { sender: "bot", content: res.data }]);
    } catch (err) {
      setMessages((prev) => [...prev, { sender: "bot", content: { error: "Upload failed" } }]);
    }
  };

  return (
    <div className="chat-window">
      <input type="file" onChange={handleUpload} />
      <div className="messages">
        {messages.map((msg, i) => (
          <ChatBubble key={i} sender={msg.sender} content={msg.content} />
        ))}
      </div>
    </div>
  );
}

export default Chatbot;