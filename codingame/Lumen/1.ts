interface Vertex {
    row: number;
    col: number;
}

const N: number = parseInt(readline());
const L: number = parseInt(readline());
let adjMatrix: number[][] = [];
let queue: Vertex[] = [];
for (let row = 0; row < N; row++) {
    const LINE: string = readline().replace(/ /g, '');
    console.error(LINE);
    adjMatrix.push([]);
    for (let col = 0; col < LINE.length; col++) {
        if (LINE[col] === 'C') {
            queue.push({row, col});
            adjMatrix[row].push(0);
        } else {
            adjMatrix[row].push(-1);
        }
    }
}

while (queue.length !== 0) {
    let cv = queue.shift(); // currentVertex
    let level = adjMatrix[cv.row][cv.col] + 1;
    for (let row = cv.row - 1; row <= cv.row + 1; row++) {
        for (let col = cv.col - 1; col <= cv.col + 1; col++) {
            if (adjMatrix[row] && adjMatrix[row][col] === -1) {
                adjMatrix[row][col] = level;
                queue.push({row, col});
            }
        }
    }
}

let unreachable = 0;
for (let row = 0; row < adjMatrix.length; row++) {
    for (let col = 0; col < adjMatrix[row].length; col++) {
        if (adjMatrix[row][col] >= L || adjMatrix[row][col] === -1) {
            unreachable++;
        }
    }
}
console.log(unreachable);
