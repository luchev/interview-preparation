const width: number = parseInt(readline()); // the number of cells on the X axis
const height: number = parseInt(readline()); // the number of cells on the Y axis
let matrix: string[] = [];
for (let i = 0; i < height; i++) {
    const line: string = readline(); // width characters, each either 0 or .
    matrix.push(line);
}

interface Point {
    x: number;
    y: number;
}

console.error(matrix);
for (let row = 0; row < height; row++) {
    for (let col = 0; col < width; col++) {
        if (matrix[row][col] === '0') {
            let right: Point = {x: -1, y: -1}
            for (let colPointer = col + 1; colPointer < width; colPointer++) {
                if (matrix[row][colPointer] === '0') {
                    right.x = row;
                    right.y = colPointer;
                    break;
                }
            }

            let bottom: Point = {x: -1, y: -1}
            for (let rowPointer = row + 1; rowPointer < height; rowPointer++) {
                if (matrix[rowPointer][col] === '0') {
                    bottom.x = rowPointer;
                    bottom.y = col;
                    break;
                }
            }
            console.log(col, row, right.y, right.x, bottom.y, bottom.x);
        }
    }
}
