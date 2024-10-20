import styles from "./SessionChatRoom.module.css";
import { useEffect, useState } from "react";
import { ChatBubble } from "../../components/non-ui/ChatBubble";
import { MobileDrawer } from "../../components/ui/MobileDrawer";
import { Delayed } from "../../components/non-ui/Delayed";
import { SCRSidebar } from "./SessionChatRoom-Sidebar";
import { Link } from "wouter";
import { Paperclip, Send, ArrowLeft } from "lucide-react";
import exampleXray from "../../assets/example-xray.webp";
import { useMutation } from "@tanstack/react-query";
import { useModelDataStore } from "../../utils/modelDataStore";

export default function SessionChatRoom({ params }) {
  const { sessionId } = params;
  const [previewImg, setPreviewImg] = useState("https://placehold.co/600x400"); // "https://placehold.co/600x400"
  const [chatMsgs, setChatMsgs] = useState([]);
  const { dataForm, setDataForm, resetDataForm } = useModelDataStore();

  const handleFiles = (e) => {
    const currentImage = e.target.files[0];
    // insert file requirements here
    setPreviewImg(URL.createObjectURL(currentImage));
  };

  const sendFormData = useMutation({
    mutationFn: (formData) =>
      fetch("http://127.0.0.1:5000/vqa", {
        mode: "cors",
        method: "POST",
        body: formData,
        // headers: corsHeader,
      }).then((res) => res.json()),

    onMutate: (variables) => {
      setChatMsgs((prev) => [...prev, { message: variables.get("question") }]);
    },

    onError: (error, variables, context) => {
      console.error(error);
      setChatMsgs((prev) => prev.slice(0, -1));
    },

    onSuccess: (data, variables, context) => {
      setChatMsgs((prev) => [
        ...prev,
        {
          message: data.answer,
          type: "answer",
          img: URL.createObjectURL(variables.get("image")),
        },
      ]);
    },
  });

  const sendNewQuestion = (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    sendFormData.mutate(formData);

    e.target.question.value = "";
  };

  useEffect(() => {
    // insert fetching from db here
    if (!dataForm) {
      return;
    }
    sendFormData.mutate(dataForm);

    return () => resetDataForm();
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
            {sendFormData.isPending && (
              <Delayed>
                <ChatBubble
                  message="Loading..."
                  type="answer"
                  img={URL.createObjectURL(sendFormData.variables.get("image"))}
                />
              </Delayed>
            )}
          </div>
          <form id={`${styles.askingForm}`} onSubmit={sendNewQuestion}>
            <div style={{ position: "relative" }}>
              <label htmlFor="image">
                <Paperclip />
              </label>
              <input
                type="file"
                name="image"
                id="image"
                accept="image/*"
                onChange={handleFiles}
                className={`${styles.imgInput}`}
                required
              />
            </div>
            <input
              type="text"
              name="question"
              id="question"
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
