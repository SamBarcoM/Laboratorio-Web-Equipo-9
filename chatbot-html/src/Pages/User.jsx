import React from "react";

class User extends React.Component{
    render(){
        return (
            <div>
                <h1>Página que simula la bienvenida del equipo de graduación</h1>
                <p>Se pueden revisar los siguientes datos basados en las preguntas de los alumnos</p>
                <ul>
                    <li>Preguntas más frecuentes</li>
                    <li>Preguntas no respondidas por el chat</li>
                    <li>Ligas abiertas</li>
                    <li>Entre otros...</li>
                </ul>
            </div>
        );
    }
}

export default User;