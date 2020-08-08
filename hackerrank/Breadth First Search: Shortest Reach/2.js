'use strict';
const fs = require('fs');

/**
 * Complexity (n = number of nodes, m = number of edges)
 * Time complexity: O(n + m)
 * Space complexity: O(n + m)
 */
function buildGraph(edges, vertexCount) {
    let graph = [];
    for (let i = 0; i < vertexCount + 1; i++) {
        graph[i] = [];
    }
    for (let pair of edges) {
        let first = pair[0];
        let second = pair[1];
        
        graph[first].push(second);
        graph[second].push(first);
    }
    return graph;
}

function bfs(n, m, edges, start) {
    let graph = buildGraph(edges, n);
    
    let distances = [];
    for (let i = 0; i < n + 1; i++) {
        distances[i] = -1;
    }
    distances[start] = 0;
    
    let visited = [];
    for (let i = 0; i < n + 1; i++) {
        visited[i] = false;
    }
    visited[start] = true;
    
    let queue = [start];
    while (queue.length != 0) {
        let current = queue.shift();
        
        let neighbourDistance = distances[current] + 6;
        for (let neighbour of graph[current]) {
            if (!visited[neighbour]) {
                visited[neighbour] = true;
                queue.push(neighbour);
                if (distances[neighbour] === -1) {
                    distances[neighbour] = neighbourDistance;
                } else {
                    distances[neighbour] = Math.min(distances[neighbour], neighbourDistance);
                }
            }
        }
    }
    
    distances.splice(start, 1); // Remove the start node distance
    distances.shift(); // Remove the 0, because we count from 1
    return distances;
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
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const q = parseInt(readLine(), 10);
    for (let qItr = 0; qItr < q; qItr++) {
        const nm = readLine().split(' ');
        const n = parseInt(nm[0], 10);
        const m = parseInt(nm[1], 10);
        let edges = Array(m);
        for (let i = 0; i < m; i++) {
            edges[i] = readLine().split(' ').map(edgesTemp => parseInt(edgesTemp, 10));
        }
        const s = parseInt(readLine(), 10);
        let result = bfs(n, m, edges, s);
        ws.write(result.join(" ") + "\n");
    }
    ws.end();
}
