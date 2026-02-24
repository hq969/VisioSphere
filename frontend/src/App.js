import React, { useState } from "react";
import VRScene from "./VRScene";
import axios from "axios";
import { startVoiceRecognition } from "./VoiceControl";

function App() {
  const [aiResponse, setAiResponse] = useState("");

  const askAI = async (prompt) => {
    const res = await axios.post("http://localhost:8000/ai-insight", {
      prompt,
    });
    setAiResponse(res.data.response);
  };

  return (
    <div>
      <h1>VisioSphere</h1>
      <button onClick={() => startVoiceRecognition(askAI)}>
        🎤 Ask AI
      </button>

      <VRScene />

      <h3>AI Insight</h3>
      <p>{aiResponse}</p>
    </div>
  );
}

export default App;
