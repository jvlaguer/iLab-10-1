import { useEffect, useState } from "react";

export const Delayed = ({ children }) => {
  const [isVisible, setVisible] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setVisible(true);
    }, 500);

    return () => clearTimeout(timer);
  });

  return isVisible ? children : null;
};
