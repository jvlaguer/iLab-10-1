import styles from "./SessionChatRoom-Sidebar.module.css";
import { Link } from "wouter";
import { ArrowLeft } from "lucide-react";

export const SCRSidebar = ({ sessionId, previewImg }) => {
  return (
    <div className={styles.sidebar}>
      <Link href="/" style={{ color: "black" }}>
        <ArrowLeft />
      </Link>
      <div className={styles.sidebarContent}>
        <h1>Medvisor Model Chatroom</h1>
        <h2>
          Current session: <strong>{sessionId}</strong>
        </h2>
      </div>
      <div>
        <p>Current Image Preview:</p>
        <img
          src={previewImg}
          alt="current image to send to the model"
          className={styles.imgPreview}
        />
      </div>
    </div>
  );
};
