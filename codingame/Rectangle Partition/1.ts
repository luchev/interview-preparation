var inputs: string[] = readline().split(' ');
const w: number = parseInt(inputs[0]);
const h: number = parseInt(inputs[1]);
const countX: number = parseInt(inputs[2]);
const countY: number = parseInt(inputs[3]);
var inputs: string[] = readline().split(' ');

let X: number[] = [0];
for (let i = 0; i < countX; i++) {
    X.push(parseInt(inputs[i]));
}
X.push(w);

let Y: number[] = [0];
var inputs: string[] = readline().split(' ');
for (let i = 0; i < countY; i++) {
    Y.push(parseInt(inputs[i]));
}
Y.push(h);

let count = 0;
for (let xStart = 0; xStart < X.length; xStart++) {
    for (let yStart = 0; yStart < Y.length; yStart++) {
        let xEnd = xStart + 1;
        let yEnd = yStart + 1;
        while (xEnd < X.length && yEnd < Y.length) {
            if (X[xEnd] - X[xStart] === Y[yEnd] - Y[yStart]) {
                count++
                xEnd++;
                yEnd++;
            } else if (X[xEnd] - X[xStart] < Y[yEnd] - Y[yStart]) {
                xEnd++;
            } else {
                yEnd++;
            }
        }
    }
}


console.log(count);
