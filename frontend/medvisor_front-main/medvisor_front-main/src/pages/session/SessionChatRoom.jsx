import styles from "./SessionChatRoom.module.css";
import { useEffect, useState } from "react";
import { ChatBubble } from "../../components/non-ui/ChatBubble";
import { MobileDrawer } from "../../components/ui/MobileDrawer";
import { SCRSidebar } from "./SessionChatRoom-Sidebar";
import { Link } from "wouter";
import { Paperclip, Send, ArrowLeft } from "lucide-react";
import exampleXray from "../../assets/example-xray.webp";

export default function SessionChatRoom({ params }) {
  const { sessionId } = params;
  const [previewImg, setPreviewImg] = useState(exampleXray); // "https://placehold.co/600x400"
  const [chatMsgs, setChatMsgs] = useState([]);

  const handleFiles = (e) => {
    const currentImage = e.target.files[0];
    // insert file requirements here
    setPreviewImg(URL.createObjectURL(currentImage));
  };

  const sendNewQuestion = (e) => {
    e.preventDefault();
    const newMsg = e.target.msgInput.value;
    e.target.msgInput.value = "";

    setChatMsgs((prev) => [...prev, { message: newMsg }]);
  };

  useEffect(() => {
    // insert fetching from db here
    // blah blah blah

    // insert data from db into chat msgs
    setChatMsgs([
      { message: "what abnormality is seen?", type: "question" },
      {
        message: "blind-ending loop of bowel arising from the cecum",
        type: "answer",
        img: exampleXray, //"https://placehold.co/30x30"
      },
    ]);
  }, []);

  return (
    <>
      <nav className={`${styles.mobileNav}`}>
        <MobileDrawer>
          <Link href="/" style={{ color: "black" }}>
            <ArrowLeft />
          </Link>
          <div>
            <h1>Medvisor Model Chatroom</h1>
            <h2>
              Current session: <strong>{sessionId}</strong>
            </h2>
          </div>
          <div>
            <p>Current Image Preview:</p>
            <img src={previewImg} alt="current image to send to the model" />
          </div>
        </MobileDrawer>
      </nav>
      <main className={styles.pageContainer}>
        <SCRSidebar sessionId={sessionId} previewImg={previewImg} />
        <div className={`${styles.content}`}>
          <div className={`${styles.chatHistory}`}>
            Chat History of Session [{sessionId}]
            {chatMsgs.map((props, index) => (
              <ChatBubble key={index} {...props} />
            ))}
          </div>
          <form id={`${styles.askingForm}`} onSubmit={sendNewQuestion}>
            <div style={{ position: "relative" }}>
              <label htmlFor="imgInput">
                <Paperclip />
              </label>
              <input
                type="file"
                name="imgInput"
                id="imgInput"
                onChange={handleFiles}
                className={`${styles.imgInput}`}
              />
            </div>
            <input
              type="text"
              name="msgInput"
              id="msgInput"
              placeholder="Enter your question"
              className={`${styles.msgInput}`}
              required
            />
            <button type="submit">
              <Send />
            </button>
          </form>
        </div>
      </main>
    </>
  );
}
