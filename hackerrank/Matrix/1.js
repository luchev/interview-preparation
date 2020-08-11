'use strict';
const fs = require('fs');

/**
 * Complexity (n = roads (edges) = vertices - 1, because it's a tree)
 * Time complexity: O(n * log(n))
 * Space complexity: O(n)
 */
function minTime(roads, machines) {
    // Sory by time for reverse kruskal
    roads.sort((a, b) => a[2] - b[2]);
    
    // Make set of the machine nodes for quick access
    let machineSet = new Set();
    for (let machine of machines) {
        machineSet.add(machine);
    }
    
    let total = 0;
    let ds = new DisjointSet(roads.length + 1, machines);
    while (roads.length > 0) {
        let edge = roads.pop();
        
        let start = edge[0];
        let end = edge[1];
        let time = edge[2];
        
        if (ds.hasMachine(start) && ds.hasMachine(end)) {
            total += time;
        } else {
            ds.join(start, end);
        }
    }
    
    return total;
}

class DisjointSet {
    constructor(size, machines) {
        this.size = size;
        
        this.parents = [];
        for (let i = 0; i < size; i++) {
            this.parents.push(i);
        }
        
        this.machineSet = new Set();
        for (let machine of machines) {
            this.machineSet.add(machine);
        }
    }
    
    join(a, b) {
        a = this.getRoot(a);
        b = this.getRoot(b);
        
        if (this.hasMachine(a)) {
            this.machineSet.add(b);
        }
        if (this.hasMachine(b)) {
            this.machineSet.add(a);
        }
        
        this.parents[a] = b;
    }
    
    getRoot(vertex) {
        if (this.parents[vertex] === vertex) {
            return vertex;
        }
        
        this.parents[vertex] = this.getRoot(this.parents[vertex]);
        
        return this.parents[vertex];
    }
    
    hasMachine(vertex) {
        return this.machineSet.has(this.getRoot(vertex));
    }
}

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const nk = readLine().split(' ');
    const n = parseInt(nk[0], 10);
    const k = parseInt(nk[1], 10);
    let roads = Array(n - 1);
    for (let i = 0; i < n - 1; i++) {
        roads[i] = readLine().split(' ').map(roadsTemp => parseInt(roadsTemp, 10));
        // Thi is modification for the broken test #2 in hacker rank
        if (roads[i].length != 3) {
            roads[i] = readLine().split(' ').map(roadsTemp => parseInt(roadsTemp, 10));
        }
    }
    let machines = [];
    for (let i = 0; i < k; i++) {
        const machinesItem = parseInt(readLine(), 10);
        machines.push(machinesItem);
    }
    const result = minTime(roads, machines);
    ws.write(result + '\n');
    ws.end();
}
