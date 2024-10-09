import styles from "./MobileDrawer.module.css";
import {
  Dialog,
  DialogTrigger,
  DialogPortal,
  DialogContent,
  DialogClose,
  DialogOverlay,
  DialogTitle,
} from "@radix-ui/react-dialog";
import { VisuallyHidden } from "@radix-ui/react-visually-hidden";
import { Menu, X } from "lucide-react";
import { useState } from "react";

export const MobileDrawer = ({ children }) => {
  const [portalContainer, setPortalContainer] = useState(null);

  return (
    <>
      <Dialog>
        <DialogTrigger className={`${styles.DialogTrigger}`}>
          <Menu /> MedVisor
        </DialogTrigger>
        <DialogPortal container={portalContainer}>
          <DialogOverlay className={`${styles.DialogOverlay}`} />
          <DialogContent
            aria-describedby={undefined}
            className={`${styles.DialogContent}`}
          >
            <VisuallyHidden asChild>
              <DialogTitle>Medvisor Nav Menu</DialogTitle>
            </VisuallyHidden>
            <div>{children}</div>
            <DialogClose className={`${styles.DialogClose}`} asChild>
              <X />
            </DialogClose>
          </DialogContent>
        </DialogPortal>
      </Dialog>

      <div ref={setPortalContainer} />
    </>
  );
};
