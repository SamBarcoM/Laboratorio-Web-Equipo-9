import React from 'react';
import './App.css';
import Home from "./Pages/Home"
import User from "./Pages/User"
import LandingPage from "./Pages/LandingPage"
import NavBar from "./Components/NavBar"
import ReactHtmlParser from "react-html-parser";
import { Widget, renderCustomComponent } from "react-chat-widget";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import * as axios from 'axios';

import 'react-chat-widget/lib/styles.css';
import './Components/chat.css';

class CustomComponent extends React.Component {
  render() {
    return (
      <div className="speech-bubble">
        {ReactHtmlParser(this.props.custom)}
      </div>
    );
  }
}

function App() {
	const handleNewUserMessage = async (message) => {
		const { data } = await axios.post('http://127.0.0.1:5002/getMessage', {
			message
		});

    renderCustomComponent(CustomComponent, { custom: data.text} );
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
      {/* <CustomChatbot />  */}
      <Widget handleNewUserMessage={handleNewUserMessage}
        title="Chatbot"
        subtitle= "Hola! Esta es la tarea 3."
      />
      
    </Router>
  );
}

export default App;
