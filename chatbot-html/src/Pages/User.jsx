import React from "react";
import {
    VictoryAnimation,
    VictoryArea,
    VictoryBar,
    VictoryChart,
    VictoryLabel,
    VictoryPie,
    VictoryStack,
    VictoryTheme,
} from 'victory';
import WordCloud from 'react-d3-cloud';

class User extends React.Component{
    render(){
        // *** Hardcode chart details for now. ***
        
        // (AreaGraph) # of Users using this features.
        const sampleNoUsersUsingFeature = [
          { x: 1, y: 2, y0: 0 },
          { x: 2, y: 3, y0: 1 },
          { x: 3, y: 5, y0: 1 },
          { x: 4, y: 4, y0: 2 },
          { x: 5, y: 6, y0: 2 }
        ];

        // (WordCloud) Where users are stuck in intent.
        const sampleStuckOnIntent = [
            { text: 'Hey', value: 1000 },
            { text: 'Chris', value: 1000 },
            { text: 'Kevin', value: 10 },
            { text: 'Samantha', value: 100000000 },
            { text: 'Emilio', value: 20 },
            { text: 'lol', value: 200 },
            { text: 'first impression', value: 800 },
            { text: 'very cool', value: 1000000 },
            { text: 'duck', value: 10 },
        ];
        const sampleFontSizeMapper = word => Math.log2(word.value) * 5;
        const sampleRotate = word => word.value % 360;

        // (Bargraph) People missing certain requirements.
        const sampleNoIntentAsking = [
            { x: 1, y: 2, y0: 0 },
            { x: 2, y: 3, y0: 0 },
            { x: 3, y: 5, y0: 0 },
            { x: 4, y: 4, y0: 0 },
            { x: 5, y: 6, y0: 0 }
        ];
        
        // (StackedBarGraph) Overall status of students missing items by CAREER.

        // (CircularProgressBar) % of students ready to graduate.
        const samplePercentageCompletedUsers = 25;
        const samplePercentageData = [{ x: 1, y: samplePercentageCompletedUsers }, { x: 2, y: 100 - samplePercentageCompletedUsers }];

        return (
            <div>
                <h1>Página que simula la bienvenida del equipo de graduación</h1>
                <p>Se pueden revisar los siguientes datos basados en las preguntas de los alumnos</p>
                <VictoryChart theme={VictoryTheme.material}>
                    <VictoryArea style={{ data: { fill: "#c43a31" }}} data={sampleNoUsersUsingFeature}/>
                </VictoryChart>
                <WordCloud
                    data= {sampleStuckOnIntent}
                    fontSizeMapper={sampleFontSizeMapper}
                    rotate={sampleRotate}
                />
                <VictoryChart
                    theme={VictoryTheme.material}
                    domainPadding={10}
                >
                    <VictoryBar style={{ data: { fill: "#c43a31" }}} data={sampleNoIntentAsking}/>
                </VictoryChart>
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
                <svg viewBox="0 0 400 400" width="100%" height="100%">
                    <VictoryPie
                        standalone={false}
                        animate={{ duration: 1000 }}
                        width={400} height={400}
                        data={samplePercentageData}
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
                    <VictoryAnimation duration={1000} data={{ percent: samplePercentageCompletedUsers, data: samplePercentageData }}>
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