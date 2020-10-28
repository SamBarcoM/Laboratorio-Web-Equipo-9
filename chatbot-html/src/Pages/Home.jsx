import React from "react";
import './Home.css';
import Card from '../Components/Card/Card';
import { ListGroup, Tabs, Tab, Table } from "react-bootstrap";
import { faTh, faUsers } from '@fortawesome/free-solid-svg-icons';
import "bootstrap/dist/css/bootstrap.min.css"

class Home extends React.Component{
    render () {
        return (
            <div className="wrapper">
                <div className="wrapper__content">
                    <Card title="TEC APPS" description="Encuentra servicios, herramientas y plataformas que tenemos disponibles para ti." icon={faTh} iconColor="#CED82D">
                        <Tabs defaultActiveKey="home" id="uncontrolled-tab-example">
                            <Tab eventKey="home" title="Tus favoritos">
                                <ListGroup>
                                    <ListGroup.Item style={{ display: "flex", justifyContent: "space-between" }}>
                                        <img src="https://mitec.itesm.mx/PublishingImages/MiTEC/Reglamento%20General%20del%20Servicio%20Social%20para%20Alumnos%20del%20Tecnol%C3%B3gico%20de%20Monterrey.png?RenditionID=5" />
                                        Servicio social
                                    </ListGroup.Item>
                                    <ListGroup.Item style={{ display: "flex", justifyContent: "space-between" }}>
                                        <img src="https://mitec.itesm.mx/PublishingImages/MiTEC/tiendavirturaltutorial.png?RenditionID=5" />
                                        Tutorial
                                    </ListGroup.Item>
                                    <ListGroup.Item style={{ display: "flex", justifyContent: "space-between" }}>
                                        <img src="https://mitec.itesm.mx/PublishingImages/MiTEC/reglamentos.png?RenditionID=5" />
                                        On Campus jobs
                                    </ListGroup.Item>
                                </ListGroup>
                            </Tab>
                            <Tab eventKey="profile" title="Recomendados">
                            </Tab>
                        </Tabs>
                    </Card>
                    <Card title="CALIFICACIONES Y HORARIOS" description="Resumen de tu información mas importante como alumno." icon={faUsers} iconColor="#F4443A">
                        <Tabs defaultActiveKey="boleta" id="uncontrolled-tab-example">
                            <Tab eventKey="boleta" title="Mi boleta">
                                <Table striped bordered hover>
                                    <thead>
                                        <tr>
                                            <th>Materias</th>
                                            <th>Faltas</th>
                                            <th>Calificación</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>Gráficas Computacionales</td>
                                            <td>0</td>
                                            <td>100</td>
                                        </tr>
                                        <tr>
                                            <td>Laboratorio de Desarrollo Web</td>
                                            <td>0</td>
                                            <td>100</td>
                                        </tr>
                                    </tbody>
                                </Table>
                            </Tab>
                            <Tab eventKey="horarios" title="Mis horarios">
                            </Tab>
                            <Tab eventKey="profesores" title="Mis profesores">
                            </Tab>
                        </Tabs>
                    </Card>
                    <Card title="ACCIONES ANTE COVID-19" description="Colaborando juntos en la continuidad académica">
                        <ListGroup.Item variant="warning">Tec de Monterrey</ListGroup.Item>
                        <ListGroup.Item variant="info">TQueremos</ListGroup.Item>
                        <ListGroup.Item variant="light">Materiales de consulta</ListGroup.Item>
                        <ListGroup.Item variant="dark">EscuchandoTec</ListGroup.Item>
                    </Card>
                </div>
            </div>
        );
    }
}
export default Home;
