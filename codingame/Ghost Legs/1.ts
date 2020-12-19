var inputs: string[] = readline().split(' ');
const W: number = parseInt(inputs[0]);
const H: number = parseInt(inputs[1]);
const matrix: string[] = [];
for (let i = 0; i < H; i++) {
    const line: string = readline();
    matrix.push(line);
}

for (let i = 0; i < matrix[0].length; i += 3) {
    let start = matrix[0][i];
    let currentCol = i;
    for (let row = 1; row < matrix.length; row++) {
        if (matrix[row][currentCol - 1] === '-') {
            currentCol -= 3;
        } else if (matrix[row][currentCol + 1] === '-') {
            currentCol += 3;
        }
    }
    let end = matrix[matrix.length - 1][currentCol];
    console.log(start + end);
}
