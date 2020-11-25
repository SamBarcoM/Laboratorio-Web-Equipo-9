import React from "react";
import {
  Border,
    VictoryAnimation,
    VictoryArea,
    VictoryBar,
    VictoryChart,
    VictoryLabel,
    VictoryLegend,
    VictoryPie,
    VictoryStack,
    VictoryTheme,
} from 'victory';
import WordCloud from 'react-d3-cloud';
import axios from 'axios';
import {Container, Button, Row, Col, Card } from 'react-bootstrap';
// import './User.css';

class User extends React.Component{
    state = {
        sampleNoIntentAsking: null,
        samplePercentageCompletedUsers: null,
        samplePercentageData: null,
        sampleNoUsersUsingFeature: null,
        sampleStuckOnIntent:[]
    }

    async componentDidMount() {
        const { data } = await axios.get('http://127.0.0.1:5002/charts');
        this.setState({
           sampleNoIntentAsking: data.no_missing_per_reqs,
           samplePercentageCompletedUsers: data.percentage_student_to_graduate,
           samplePercentageData: this.calculateCircularData(data.percentage_student_to_graduate),
           sampleNoUsersUsingFeature: data.unique_users_per_month,
           sampleStuckOnIntent: data.entity_word_cloud

        });
    }

    calculateCircularData(percent) {
        return [{ x: 1, y: percent }, { x: 2, y: 100 - percent }];
    }

    render(){
        // *** Hardcode chart details for now. ***
        
        // (AreaGraph) # of Users using this features.

        // (WordCloud) Where users are stuck in intent.
        const sampleStuckOnIntent = [
          { text: 'Photography', value: 100 },
          { text: 'CENEVAL', value: 200 },
          { text: 'E-sign', value: 3 }
        ];

        const sampleFontSizeMapper = word => Math.log2(word.value) * 10;
        const sampleRotate = word => 0;

        // (Bargraph) People missing certain requirements.
        
        // (StackedBarGraph) Overall status of students missing items by CAREER.

        // (CircularProgressBar) % of students ready to graduate.

        return (
          <Container>
            <div>
              <Row>
                <Col>
                  <h1>Data Analisis</h1>
                </Col>
              </Row>
              <Row>
                {/* <p>Se pueden revisar los siguientes datos basados en las preguntas de los alumnos</p> */}
                <Col>
                <Card border="primary" style={{ width: '66rem' }}>
                    <Card.Header>WordCloud of most asked requirements</Card.Header>
                    <Card.Body>
                      <Card.Title>Requisitos mas buscados</Card.Title>
                      <div className="wordCloudClass">
                  <WordCloud
                      data= {this.state.sampleStuckOnIntent}
                      // data= {sampleStuckOnIntent}
                      fontSizeMapper={sampleFontSizeMapper}
                      rotate={sampleRotate}
                      
                  />
                  </div>
                    </Card.Body>
                  </Card>
                </Col>
              </Row>
              <Row>
                <Col>
                  <Card border="primary" style={{ width: '30rem' }}>
                    <Card.Header>Usage</Card.Header>
                    <Card.Body>
                      <Card.Title>Porcentage de Estudiantes Utilizando Herramienta</Card.Title>
                        <VictoryChart title="Hello" theme={VictoryTheme.material}  style={{ parent: { maxWidth: "100%" },  border: { stroke: "black" } }}>
                          <VictoryArea style={{ data: { fill: "#c43a31" }}} data={this.state.sampleNoUsersUsingFeature}/>
                      </VictoryChart>
                    </Card.Body>
                  </Card>
                </Col>
                <Col>
                  <Card border="primary" style={{ width: '30rem' }}>
                    <Card.Header>Missing Student Information</Card.Header>
                    <Card.Body>
                      <Card.Title>Numero de Estudiantes que faltan de terminar requerimiento</Card.Title>
                        <VictoryChart
                        theme={VictoryTheme.material}
                        domainPadding={10}
                        >
                          <VictoryBar style={{ data: { fill: "#c43a31" }}} data={this.state.sampleNoIntentAsking}/>
                      </VictoryChart>
                    </Card.Body>
                  </Card>
                </Col>
              </Row>
              <Row>
              <Col>
                  <Card border="primary" style={{ width: '30rem' }}>
                    <Card.Header>Missing Information per Campus LEGEND</Card.Header>
                    <Card.Body>
                      <Card.Title>Legend</Card.Title>
                      <VictoryLegend x={0} y={0}
                            orientation="horizontal"
                            gutter={20}
                            itemsPerRow={3}
                            colorScale={["#334d5c","#45b29d","#efc94c","#e37c4a","#df5a49","#4f7da1","#55dbc1","#efda97","#e2a37f","#df948a"]}
                            data={[
                              { name: "Career Exam" }, { name: "E-sign" }, { name: "Education Credit" }, { name: "English Exam" }, { name: "Financial Services" }, { name: "Graduation Request" }, { name: "Library" }, { name: "Photography" }, { name: "Program" }, { name: "Social Service" }
                            ]}
                          />
                    </Card.Body>
                  </Card>
                </Col>
                <Col>
                  <Card border="primary" style={{ width: '30rem' }}>
                    <Card.Header>Missing Information per Campus</Card.Header>
                    <Card.Body>
                      <Card.Title>Numero de Estudiantes que faltan por completar requisito por campus</Card.Title>
                        <VictoryChart domainPadding={{x:50}}>
                          <VictoryStack colorScale={["#334d5c","#45b29d","#efc94c","#e37c4a","#df5a49","#4f7da1","#55dbc1","#efda97","#e2a37f","#df948a"]}>

                            <VictoryBar
                              // Career Exam
                              data={[{x: "CEM", y: 30}, {x: "CSF", y: 10}, {x: "CCM", y: 15}]}
                            />
                            <VictoryBar
                              // E-sign
                              data={[{x: "CEM", y: 25}, {x: "CSF", y: 9}, {x: "CCM", y: 16}]}
                            />
                            <VictoryBar
                              // Education Credit
                              data={[{x: "CEM", y: 23}, {x: "CSF", y: 5}, {x: "CCM", y: 13}]}
                            /> 
                            <VictoryBar
                              // English Exam
                              data={[{x: "CEM", y: 23}, {x: "CSF", y: 5}, {x: "CCM", y: 13}]}
                            /> 
                            <VictoryBar
                              // Financial Services
                              data={[{x: "CEM", y: 23}, {x: "CSF", y: 5}, {x: "CCM", y: 13}]}
                            /> 
                            <VictoryBar
                              // Graduation Request
                              data={[{x: "CEM", y: 23}, {x: "CSF", y: 5}, {x: "CCM", y: 13}]}
                            /> 
                            <VictoryBar
                              // Library
                              data={[{x: "CEM", y: 23}, {x: "CSF", y: 5}, {x: "CCM", y: 13}]}
                            /> 
                            <VictoryBar
                              // Photography
                              data={[{x: "CEM", y: 23}, {x: "CSF", y: 5}, {x: "CCM", y: 13}]}
                            /> 
                            <VictoryBar
                              // Program
                              data={[{x: "CEM", y: 23}, {x: "CSF", y: 5}, {x: "CCM", y: 13}]}
                            /> 
                            <VictoryBar
                              // Social Service
                              data={[{x: "CEM", y: 23}, {x: "CSF", y: 5}, {x: "CCM", y: 13}]}
                            /> 
                          </VictoryStack>
                        </VictoryChart>

                    </Card.Body>
                  </Card>
                </Col>

                <Col>
                  <Card border="primary" style={{ width: '30rem' }}>
                    <Card.Header>Completion Percent</Card.Header>
                    <Card.Body>
                      <Card.Title>Porcentage de estudiantes con Requerimientos completos</Card.Title>
                      <svg viewBox="0 0 400 400" width="100%" height="100%">
                      <VictoryPie
                          standalone={false}
                          animate={{ duration: 1000 }}
                          width={400} height={400}
                          data={this.state.samplePercentageData}
                          innerRadius={120}
                          cornerRadius={25}
                          labels={() => null}
                          style={{
                            data: { fill: ({ datum }) => {
                              const color = datum.y > 30 ? "green" : "red";
                              return datum.x === 1 ? color : "transparent";
                            }
                            }
                          }}
                      />
                      <VictoryAnimation duration={1000} data={{ percent: this.state.samplePercentageCompletedUsers, data: this.state.samplePercentageData }}>
                          {(newProps) => {
                            return (
                              <VictoryLabel
                                textAnchor="middle" verticalAnchor="middle"
                                x={200} y={200}
                                text={`${Math.round(newProps.percent)}%`}
                                style={{ fontSize: 45 }}
                              />
                            );
                          }}
                      </VictoryAnimation>
                  </svg>
                    </Card.Body>
                  </Card>
                </Col>
              </Row>
              {/* <Row>
                <Col>
                  <h3>Porcentage de Estudiantes Utilizando Herramienta</h3>
                </Col>
                <Col>
                  <h3>Numero de Estudiantes que faltan de terminar requerimiento</h3>
                </Col>
              </Row>
                
              <Row>
                <Col>
                  <VictoryChart title="Hello" theme={VictoryTheme.material}  style={{ parent: { maxWidth: "100%" },  border: { stroke: "black" } }}>
                      <VictoryArea style={{ data: { fill: "#c43a31" }}} data={this.state.sampleNoUsersUsingFeature}/>
                  </VictoryChart>
                </Col>
                <Col>
                  <VictoryChart
                      theme={VictoryTheme.material}
                      domainPadding={10}
                  >
                      <VictoryBar style={{ data: { fill: "#c43a31" }}} data={this.state.sampleNoIntentAsking}/>
                  </VictoryChart>
                </Col>
              </Row>
              <Row>
                <Col>
                  <h3>Numero de Estudiantes que faltan por completar requisito por campus</h3>
                </Col>
                <Col>
                  <h3>Porcentage de estudiantes con Requerimientos completos</h3>
                </Col>
              </Row>
              <Row>
                <Col>
                <VictoryStack colorScale={["tomato", "orange", "gold"]}>
                    <VictoryBar
                      data={[{x: "a", y: 2}, {x: "b", y: 3}, {x: "c", y: 5}]}
                    />
                    <VictoryBar
                      data={[{x: "a", y: 1}, {x: "b", y: 4}, {x: "c", y: 5}]}
                    />
                    <VictoryBar
                      data={[{x: "a", y: 3}, {x: "b", y: 2}, {x: "c", y: 6}]}
                    /> 
                </VictoryStack>
                </Col>
                <Col>
                  <svg viewBox="0 0 400 400" width="100%" height="100%">
                      <VictoryPie
                          standalone={false}
                          animate={{ duration: 1000 }}
                          width={400} height={400}
                          data={this.state.samplePercentageData}
                          innerRadius={120}
                          cornerRadius={25}
                          labels={() => null}
                          style={{
                            data: { fill: ({ datum }) => {
                              const color = datum.y > 30 ? "green" : "red";
                              return datum.x === 1 ? color : "transparent";
                            }
                            }
                          }}
                      />
                      <VictoryAnimation duration={1000} data={{ percent: this.state.samplePercentageCompletedUsers, data: this.state.samplePercentageData }}>
                          {(newProps) => {
                            return (
                              <VictoryLabel
                                textAnchor="middle" verticalAnchor="middle"
                                x={200} y={200}
                                text={`${Math.round(newProps.percent)}%`}
                                style={{ fontSize: 45 }}
                              />
                            );
                          }}
                      </VictoryAnimation>
                  </svg>
                </Col>
              </Row> */}
              <Row>
                {/* <Col>
                  <h3>Porcentage de Estudiantes Utilizando Herramienta</h3>
                </Col> */}
              </Row>
            </div>
          </Container>
        );
    }
}

export default User;