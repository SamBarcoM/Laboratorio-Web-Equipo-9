import React from 'react';
import './App.css';
import Home from "./Pages/Home"
import User from "./Pages/User"
import LandingPage from "./Pages/LandingPage"
import NavBar from "./Components/NavBar"
// import CustomChatbot from "./Components/CustomChatbot"
import 'react-chat-widget/lib/styles.css';
import { Widget, addResponseMessage } from "react-chat-widget";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import * as axios from 'axios';

function App() {
	const handleNewUserMessage = async (message) => {
		const { data } = await axios.post('http://127.0.0.1:5002/getMessage', {
			message
		});

		addResponseMessage(data.text);
	}

  return (
    <Router>
      <NavBar/>
      <Switch>
        <Route path="/home">
          <Home />
        </Route>
        <Route path="/user">
          <User />
        </Route>
        <Route exact path="/">
          <LandingPage />
        </Route>
      </Switch>
      
      <Widget handleNewUserMessage={handleNewUserMessage}
        title="Chatbot"
        subtitle= "Hola! Esta es la tarea 3."
      />
      
    </Router>
  );
}

export default App;
