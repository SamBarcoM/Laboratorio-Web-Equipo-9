import React from 'react';
import { Navbar, Nav, Form, FormControl, Button} from "react-bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"
import "./NavBar.css"

import { useAuth0 } from '@auth0/auth0-react';

const Profile= () =>{
    const { user, isAuthenticated, isLoading, loginWithRedirect } = useAuth0();
    

    if(isLoading){
        return "";
    }
    if(isAuthenticated){
        return <LogoutButton></LogoutButton>;
    }
    else{
        loginWithRedirect();
        return <LoginButton></LoginButton>;
    }
}

const LoginButton = () =>{
    const { loginWithRedirect } = useAuth0();
    return(
        <button onClick={()=>loginWithRedirect()}>
            Login
        </button>
    );
};

const LogoutButton = () =>{
    const { logout } = useAuth0();
    return (
        <Button bg="dark" variant="outline-light" onClick={() => logout({ returnTo: window.location.orgin })}>
            Logout
        </Button>
    );
};

class NavBar extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            search: "Qué buscamos...",
        };
    }
    // Funci[on lambda s[i asigna valor => funcion lambda, sin flecha no lo asigna
    searchItem = (params) => {
        console.log(params.target.value);
        this.setState({
            search: params.target.value,
        })
    }

    render (){
            return (
                <Navbar bg="tec" variant="dark">
                    <Navbar.Brand href="/">Proyecto Web</Navbar.Brand>
                    <Nav className="mr-auto">
                        <Nav.Link href="/home">miTec</Nav.Link>
                        <Nav.Link href="/user">Administradores</Nav.Link>
                        <Nav.Link href="/graficas">Gráficas</Nav.Link>
                        <Nav.Link href="/">{this.state.search}</Nav.Link>
                    </Nav>
                    <Form inline>
                        <FormControl onChange={this.searchItem} type="text" placeholder="Search" className="mr-sm-2" />
                        <Button bg="dark" variant="outline-light">Search</Button>
                    </Form>
                    <Profile></Profile>
                </Navbar>     
                  
            );
        }
}

export default NavBar;
