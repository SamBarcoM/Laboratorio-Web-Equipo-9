import React from "react";
import ChatBot from "react-simple-chatbot";

function CustomChatbot(props) {
    const config = {
        width: "400px",
        height: "600px",
        floating: true
    };
      // Taken from SamBarcoM as suggestion.
      //https://lucasbassetti.com.br/react-simple-chatbot/#/docs/custom
    const steps = [
        {
            id: "Start",
            message: "Hello, welcome to our web page",
            trigger: "Get Name"
        },
        {
            id: "Get Name",
            message: "What is your name?",
            trigger: "Wait user input for name",
        },
        {
            id: "Wait user input for name",
            user: true,
            trigger: "Welcome"
        },
        {
            id: "Welcome",
            message: "Welcome {previousValue}!",
            trigger: "Suggest options",
        },
        {
            id: "Suggest options",
            message: "What kind of music would you like?",
            trigger: "Display options"
        },
        {
            id: "Display options",
            options: [
                        {
                            value: "indie",
                            label: "Indie",
                            trigger: "Indie option"
                        },
                        { 
                            value: "rock",
                            label: "Rock",
                            trigger: "Rock option"
                        }, 
                        { 
                            value: "lofi",
                            label: "Lofi",
                            trigger: "Lofi option"
                        } 
                    ]
        },
        {
            id: "Indie option",
            message: "You'll like this indie song...",
            trigger: "Indie recommendation"
        },
        {
            id: "Rock option",
            message: "You'll like this rock song...",
            trigger: "Rock recommendation"
        },
        {
            id: "Lofi option",
            message: "You'll like this lofi song...",
            trigger: "Lofi recommendation"
        },
        {
            id: "Indie recommendation",
            component: (
                <div class="card" width="100%">
                    <img class="card-img-top" src={require("../img/SALES__Renee.jpg")} alt="Sales's album cover"/>
                    <div class="card-body">
                        <h5 class="card-title">Renee, SALES</h5>
                        <p class="card-text">Listen to SALES' latest album on Spotify!</p>
                        <a href="https://open.spotify.com/track/5MeUMSRreLHYLhw8ZTyqpk" class="btn btn-primary">Listen on Spotify...</a>
                    </div>
                </div>
            ),
            trigger: "Finish"
        },
        {
            id: "Rock recommendation",
            component: (
                <div class="card" width="100%">
                <img class="card-img-top" src={require("../img/Queen__Sheer_Heart_Attack.jpg")} alt="Queen's album cover"/>
                    <div class="card-body">
                        <h5 class="card-title">Killer Queen, Queen</h5>
                        <p class="card-text">Listen to Queen's album on Spotify!</p>
                        <a href="https://open.spotify.com/track/70wvmV1Dyg1xWtCYSngm4R?si=hUFqAp55QOW4Z8WZY8-VKA" class="btn btn-primary">Listen on Spotify...</a>
                    </div>
                </div>
            ),
            trigger: "Finish"
        },
        {
            id: "Lofi recommendation",
            component: (
                <div class="card" width="100%">
                    <img class="card-img-top" src={require("../img/Feng_Suave__Venus_Flytrap.jpg")} alt="Venus Flytrap's album cover"/>
                    <div class="card-body">
                        <h5 class="card-title">Venus Flytrap, Feng Suave</h5>
                        <p class="card-text">Listen to Feng Suave's album on Spotify!</p>
                        <a href="https://open.spotify.com/track/6B1Q7hi48RVUvak1SLoiJX?si=CuGS0cl1SSWWcphw_4wzyg" class="btn btn-primary">Listen on Spotify...</a>
                    </div>
                </div>
            ),
            trigger: "Finish"
        },
        {
            id: "Finish",
            message: "Would you like a new suggestion?",
            trigger: "Displaying final options"
        },
        {
            id: "Displaying final options",
            options: [
                        {
                            value: "yes",
                            label: "Yes!",
                            trigger: "Display options"
                        },
                        { 
                            value: "no",
                            label: "No",
                            trigger: "Bye"
                        } 
                    ]
        },
        {
            id: "Bye",
            message: "It was a pleasure serving you human.\nHave a nice day!",
            end: true
        }
    ];
  return <ChatBot steps={steps} {...config} />;
}
export default CustomChatbot;