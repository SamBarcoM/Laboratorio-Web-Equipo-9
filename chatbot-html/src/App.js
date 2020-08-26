import React from 'react';
import './App.css';
import Home from "./Pages/Home"
import User from "./Pages/User"
import LandingPage from "./Pages/LandingPage"
import NavBar from "./Components/NavBar"
import CustomChatbot from "./Components/CustomChatbot"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"


function App() {

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
      <CustomChatbot />
      {/*<Widget handleNewUserMessage={handleNewUserMessage}
        title="TEC"
        subtitle= "Hola, escribe tus dudas"
      />*/} 
      
    </Router>
  );
}

export default App;