const N: number = parseInt(readline());
let strengths: number[] = [];
for (let i = 0; i < N; i++) {
    const pi: number = parseInt(readline());
    strengths.push(pi);
}

strengths.sort((a, b) => {return a - b;});

let minDif = strengths[1] - strengths[0];
for (let i = 2; i < strengths.length; i++) {
    if (strengths[i] - strengths[i - 1] < minDif) {
        minDif = strengths[i] - strengths[i - 1];
    }
}

console.log(minDif)
