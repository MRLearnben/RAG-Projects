import { useState } from "react";
import axios from "axios";

export default function App() {
  const [q, setQ] = useState("");
  const [a, setA] = useState("");

  const ask = async () => {
    const res = await axios.post("http://localhost:8000/chat/", {
      question: q
    });
    setA(res.data.answer);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Maintenance Assistant</h2>

      <input
        value={q}
        onChange={(e) => setQ(e.target.value)}
        placeholder="Ask..."
      />

      <button onClick={ask}>Ask</button>

      <p>{a}</p>
    </div>
  );
}
