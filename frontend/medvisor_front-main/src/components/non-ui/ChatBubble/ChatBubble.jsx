import styles from "./ChatBubble.module.css";

/**
 *
 * @param {string} message
 * @param {"question" | "answer"} type
 * @param {string?} img
 * @returns {ReactNode}
 */
export const ChatBubble = ({ message, type = "question", img }) => {
  const questionAnswerStyle =
    type == "question" ? styles.question : styles.answer;

  return (
    <div className={`${styles.rowContainer} ${questionAnswerStyle}`}>
      {type == "answer" && <img src={img} alt="avatar" />}
      <div className={`${styles.chatBubble} ${questionAnswerStyle}`}>
        <p>{message}</p>
      </div>
    </div>
  );
};
