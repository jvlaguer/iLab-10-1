import { Route, Switch } from "wouter";
import Home from "./pages/Home";
import SessionChatRoom from "./pages/session/SessionChatRoom";

export default function Router() {
  return (
    <Switch>
      <Route path="/" component={Home} />
      <Route path="/session/:sessionId" component={SessionChatRoom} />
      <Route>404: Page Does Not Exist!</Route>
    </Switch>
  );
}
