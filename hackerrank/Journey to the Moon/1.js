'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = number of astronauts, p = edges in the graph (astronaut pairs), p < n)
 * Time complexity: O(p + n)
 * Space complexity: O(p)
 */
function journeyToMoon( n, astronaut ) {
    // Build graph
    let graph = buildGraph( astronaut );
    // Split the graph into components
    let components = {};
    for ( let start of Object.keys( graph ) ) {
        dfs( graph, parseInt( start ), parseInt( start ), components );
    }

    // Aggregate the different graph components by summing the vertices in each component
    let countrymen = {};
    for ( let component of Object.values( components ) ) {
        if ( countrymen[component] === undefined ) {
            countrymen[component] = 1;
        } else {
            countrymen[component] += 1;
        }
    }

    // All astronauts that weren't part of the graph are from a separate country, by themselves
    let singleAstronauts = n - Object.values( countrymen ).reduce( ( total, x ) => total + x, 0 );

    // Time to calculate the combinations of pairs of astronauts from different countries
    let combinations = 0;

    // Add all the pairs of single astronauts = singleAstronauts choose 2, order is not important
    if ( singleAstronauts >= 2 ) {
        combinations += singleAstronauts * ( singleAstronauts - 1 ) / 2;
    }

    // For countries with 1+ astronaut, iteratively calculate the different pairs they can form
    let combinationsArr = Object.values( countrymen );
    while ( combinationsArr.length >= 1 ) {
        let countryAnumber = combinationsArr.shift(); // Country with 1+ astronaut X single astronaut
        combinations += countryAnumber * singleAstronauts;

        // Country with 1+ astronaut x country with 1+ astronaut
        for ( let countryBnumber of combinationsArr ) {
            combinations += countryAnumber * countryBnumber;
        }
    }

    return combinations;
}

function buildGraph( edgeList ) {
    let graph = {};
    for ( let edge of edgeList ) {
        if ( !graph[edge[0]] ) {
            graph[edge[0]] = [];
        }
        graph[edge[0]].push( edge[1] );

        if ( !graph[edge[1]] ) {
            graph[edge[1]] = [];
        }
        graph[edge[1]].push( edge[0] );
    }
    return graph;
}

function dfs( graph, currentVertex, componentId, components ) {
    if ( components[currentVertex] !== undefined ) {
        return;
    }

    components[currentVertex] = componentId;
    for ( let neighbour of graph[currentVertex] ) {
        dfs( graph, neighbour, componentId, components );
    }
}

process.stdin.resume();
process.stdin.setEncoding( 'utf-8' );

let inputString = '';
let currentLine = 0;

process.stdin.on( 'data', inputStdin => {
    inputString += inputStdin;
} );

process.stdin.on( 'end', _ => {
    inputString = inputString.replace( /\s*$/, '' )
        .split( '\n' )
        .map( str => str.replace( /\s*$/, '' ) );

    main();
} );

function readLine() {
    return inputString[currentLine++];
}

function main() {
    const ws = fs.createWriteStream( process.env.OUTPUT_PATH );
    const np = readLine().split( ' ' );
    const n = parseInt( np[0], 10 );
    const p = parseInt( np[1], 10 );
    let astronaut = Array( p );
    for ( let i = 0; i < p; i++ ) {
        astronaut[i] = readLine().split( ' ' ).map( astronautTemp => parseInt( astronautTemp, 10 ) );
    }
    let result = journeyToMoon( n, astronaut );
    ws.write( result + "\n" );
    ws.end();
}
