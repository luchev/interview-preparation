'use strict';
const fs = require('fs');

/**
 * Complexity (n = number of nodes, m = number of edges)
 * Time complexity: O(n + m)
 * Space complexity: O(n + m)
 */
function evenForest(t_nodes, t_edges, fromArr, toArr) {
    let graph = buildGraph(fromArr, toArr);
    console.log(graph);
    
    visited.add(1);
    recursiveNodeCount(graph, 1);
    
    let evenNodeSubTrees = 0;
    Object.values(nodesInSubTree).forEach(x => {
        if (x % 2 === 0) {
            evenNodeSubTrees++;
        }
    });
    return evenNodeSubTrees - 1;
}

function buildGraph(fromArr, toArr) {
    let graph = {};
    
    for (let i in fromArr) {
        if (!graph[fromArr[i]]) {
            graph[fromArr[i]] = [];
        }
        graph[fromArr[i]].push(toArr[i]);
        
        if (!graph[toArr[i]]) {
            graph[toArr[i]] = [];
        }
        graph[toArr[i]].push(fromArr[i]);
    }
    
    return graph;
}

let nodesInSubTree = {};
let visited = new Set();

function recursiveNodeCount(graph, current) {
    let isLeaf = true;
    for (let neighbour of graph[current]) {
        if (!visited.has(neighbour)) {
            visited.add(neighbour);
            recursiveNodeCount(graph, neighbour);
            isLeaf = false;
        }
    }
    
    nodesInSubTree[current] = 1; // at least 1 for the current node
    if (isLeaf) {
        return;
    }
    
    for (let neighbour of graph[current]) {
        if (nodesInSubTree[neighbour]) {
            nodesInSubTree[current] += nodesInSubTree[neighbour];
        }
    }
}

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const tNodesEdges = readLine().split(' ');
    const t_nodes = parseInt(tNodesEdges[0], 10);
    const t_edges = parseInt(tNodesEdges[1], 10);
    let t_from = [];
    let t_to = [];

    for (let i = 0; i < t_edges; i++) {
        const tFromTo = readLine().split(' ');
        t_from.push(parseInt(tFromTo[0], 10));
        t_to.push(parseInt(tFromTo[1], 10));
    }

    const res = evenForest(t_nodes, t_edges, t_from, t_to);
    ws.write(res + '\n');
    ws.end();
}
