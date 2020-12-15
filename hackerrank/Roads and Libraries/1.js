'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = cities/vertices, m = roads/edges)
 * Time complexity: O(n + m)
 * Space complexity: O(n + m)
 */
function roadsAndLibraries( n, c_lib, c_road, roads ) {
    // If building libraries is cheaper than building roads
    if ( c_lib <= c_road ) {
        return n * c_lib;
    }

    let graph = buildGraph( roads );

    let visited = [];
    let components = [];
    for ( let i = 0; i < n + 1; i++ ) {
        visited.push( false );
        components.push( i );
    }

    // Create a spanning forest
    for ( let root of Object.keys( graph ) ) {
        dfs( graph, parseInt( root ), visited, components, root );
    }

    components.shift();

    let componentCount = {};
    for ( let component of components ) {
        // Count the vertices in each spanning tree
        componentCount[component] = ( componentCount[component] || 0 ) + 1;
    }

    let roadCount = 0;
    for ( let key of Object.keys( componentCount ) ) {
        // The edges in a tree are number-of-vertices - 1
        roadCount += componentCount[key] - 1;
    }

    // Build 1 library in each component
    // console.log("Libraries: ", Object.keys(componentCount).length);
    
    // Build as many roads as you can to make spanning trees
    // console.log("Roads: ", roadCount);

    return roadCount * c_road + Object.keys( componentCount ).length * c_lib;
}

function dfs( graph, currentVertex, visited, components, root ) {
    if ( visited[currentVertex] ) {
        return;
    }
    visited[currentVertex] = true;
    components[currentVertex] = root;

    for ( let neighbour of graph[currentVertex] ) {
        dfs( graph, neighbour, visited, components, root );
    }

}

function buildGraph( edgeList ) {
    let graph = {};
    for ( let edge of edgeList ) {
        if ( graph[edge[0]] === undefined ) {
            graph[edge[0]] = [];
        }
        graph[edge[0]].push( edge[1] );

        if ( graph[edge[1]] === undefined ) {
            graph[edge[1]] = [];
        }
        graph[edge[1]].push( edge[0] );
    }

    return graph;
}

process.stdin.resume();
process.stdin.setEncoding( 'utf-8' );

let inputString = '';
let currentLine = 0;

process.stdin.on( 'data', inputStdin => {
    inputString += inputStdin;
} );

process.stdin.on( 'end', function () {
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
    const q = parseInt( readLine(), 10 );
    for ( let qItr = 0; qItr < q; qItr++ ) {
        const nmC_libC_road = readLine().split( ' ' );
        const n = parseInt( nmC_libC_road[0], 10 );
        const m = parseInt( nmC_libC_road[1], 10 );
        const c_lib = parseInt( nmC_libC_road[2], 10 );
        const c_road = parseInt( nmC_libC_road[3], 10 );
        let cities = Array( m );
        for ( let i = 0; i < m; i++ ) {
            cities[i] = readLine().split( ' ' ).map( citiesTemp => parseInt( citiesTemp, 10 ) );
        }
        const result = roadsAndLibraries( n, c_lib, c_road, cities );
        ws.write( result + '\n' );
    }
    ws.end();
}
