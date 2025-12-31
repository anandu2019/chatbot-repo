import React from "react";

function ChatBubble({ sender, content }) {
  const isBot = sender === "bot";

  return (
    <div className={`bubble ${isBot ? "bot" : "user"}`}>
      {typeof content === "object" && !content.error ? (
        <table>
          <tbody>
            {Object.entries(content).map(([key, value]) => (
              <tr key={key}>
                <td><strong>{key}</strong></td>
                <td>{Array.isArray(value) ? value.join(", ") : value}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>{typeof content === "string" ? content : content.error}</p>
      )}
    </div>
  );
}

export default ChatBubble;