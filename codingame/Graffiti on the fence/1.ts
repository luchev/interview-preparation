const L: number = parseInt(readline());
const N: number = parseInt(readline());
let start = {};
let end = {};
let points: number[] = [0];

for (let i = 0; i < N; i++) {
    var inputs: string[] = readline().split(' ');
    const st: number = parseInt(inputs[0]);
    if (start[st]) {
        start[st]++;
    } else {
        start[st] = 1;
    }
    const ed: number = parseInt(inputs[1]);
    if (end[ed]) {
        end[ed]++;
    } else {
        end[ed] = 1;
    }
    points.push(st);
    points.push(ed);
}
points.push(L);
points.sort((a, b) => a - b);
let uniquePoints = [points[0]];
for (let i = 1; i < points.length; i++) {
    if (points[i] !== points[i - 1]) {
        uniquePoints.push(points[i]);
    }
}
points = uniquePoints;

let toBePaintedCount = 0;
let beginPaint = 0;
let endPaint = -1;
let painting = false;
let insidePaintRegions = 0;
for (let i of points) {
    if (start[i]) {
        insidePaintRegions += start[i];
    }
    if (end[i]) {
        insidePaintRegions -= end[i];
    }

    if (!painting && !start[i] && insidePaintRegions === 0) {
        painting = true;
        beginPaint = i;
    }

    if (start[i] && painting) {
        painting = false;
        endPaint = i;
        if (endPaint > beginPaint) {
            console.log(beginPaint, endPaint);
        }
        toBePaintedCount++;
    }
}
console.error(beginPaint, L);
if (painting && beginPaint < L) {
    console.log(beginPaint, L);
    toBePaintedCount++;
}

if (toBePaintedCount === 0) {
    console.log("All painted");
}
