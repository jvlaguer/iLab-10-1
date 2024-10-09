import { useState } from "react";
import { Link, useLocation } from "wouter";
import style from "./Home.module.css";

function Home() {
  const [existingSessionId, setExistingSessionId] = useState("");
  const [location, setLocation] = useLocation();

  return (
    <main className={style.page}>
      <div id={style.container}>
        <div id={style.spiel}>
          <h1>MedVisor</h1>
          <p>
            Welcome! Please upload a medical image and enter your question below
            to begin a Visual Question Answering session
          </p>
        </div>

        <form action="/">
          <input
            type="file"
            accept="image/*"
            name="model-image"
            id="model-image"
            className={style.modelImage}
            required
          />
          <div>
            <textarea
              name="model-question"
              id="model-question"
              cols="65"
              placeholder="Enter your question"
              wrap="soft"
              maxLength={300}
              required
            />
            <label htmlFor="model-question">Max 300 Characters</label>
          </div>
          <button type="submit">SUBMIT</button>
        </form>

        <hr />

        <div id={style.resumeSessionContainer}>
          <p>Or resume a previous session</p>
          <div id={style.resumeSession}>
            <input
              onChange={(e) => setExistingSessionId(e.target.value)}
              value={existingSessionId}
              type="text"
              placeholder="Session ID"
            />
            <button
              onClick={() => setLocation(`/session/${existingSessionId}`)}
              disabled={!existingSessionId}
            >
              RESUME SESSION
            </button>
          </div>
        </div>
      </div>
    </main>
  );
}

export default Home;
