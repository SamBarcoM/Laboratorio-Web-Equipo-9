import React from "react";
import ChatBot from "react-simple-chatbot";
function CustomChatbot(props) {
    const config = {
        width: "400px",
        height: "600px",
        floating: true
    };
      //https://lucasbassetti.com.br/react-simple-chatbot/#/docs/custom
    const steps = [
        {
            id: "Greet",
            message: "Hello, Welcome to our web page",
            trigger: "Ask Name"
        },
        {
            id: "Ask Name",
            message: "What is your name?",
            trigger: "Waiting user input for name",
        },
        {
                id: "Waiting user input for name",
                user: true,
                trigger: "Welcome"
        },
        {
            id: "Welcome",
            message: "Welcome {previousValue}!",
            trigger: "Asking options to suggest",
        },
        {
            id: "Asking options to suggest",
            message: "What would you like to discover?",
            trigger: "Displaying options"
        },
        {
            id: "Displaying options",
            options: [
                        {
                            value: "music",
                            label: "Music",
                            trigger: "Asking for Music"
                        },
                        { 
                            value: "movies",
                            label: "Movies",
                            trigger: "Asking for Movie"
                        } 
                    ]
        },
        {
            id: "Asking for Music",
            message: "I would recommend you this song...",
            trigger: "Music recommendation"
        },
        {
            id: "Asking for Movie",
            message: "I would recommend you this movie...",
            trigger: "Movie recommendation"
        },
        {
            id: "Music recommendation",
            component: (
                <div class="card" width="100%">
                    <img class="card-img-top" src={require("../img/folklore.png")} alt="Taylor's album cover"/>
                    <div class="card-body">
                        <h5 class="card-title">Betty, Taylor Swift</h5>
                        <p class="card-text">Listen to Taylor's latest album on Spotify!</p>
                        <a href="https://open.spotify.com/track/0x3CUvkL4jUPYVONrYUubR?si=UT9iZZ4QRIGSuYeyG3tm6A" class="btn btn-primary">Listen on Spotify...</a>
                    </div>
                </div>
            ),
            trigger: "Done"
        },
        {
            id: "Movie recommendation",
            component: (
                <div class="card" width="100%">
                    <img class="card-img-top" src={require("../img/disney.jpg")} alt="The Lady and the tramp"/>
                    <div class="card-body">
                        <h5 class="card-title">The Lady and the Tramp, Disney 2019</h5>
                        <p class="card-text">Are you into classics? We suggest you Disney's latest live-action The Lady and the Tramp!</p>
                        <a href="https://www.youtube.com/watch?v=ma_8wedSR_o" class="btn btn-primary">Watch the trailer...</a>
                    </div>
                </div>
            ),
            trigger: "Done"
        },
        {
            id: "Done",
            message: "Would you like a new suggestion?",
            trigger: "Displaying final options"
        },
        {
            id: "Displaying final options",
            options: [
                        {
                            value: "yes",
                            label: "Yes!",
                            trigger: "Asking options to suggest"
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
            message: "I hope you enjoy the suggestions.\nBye, have a nice day!",
            end: true
        }
    ];
  return <ChatBot steps={steps} {...config} />;
}
export default CustomChatbot;