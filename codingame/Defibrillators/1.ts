const LON: number = parseFloat(readline().replace(',', '.'));
const LAT: number = parseFloat(readline().replace(',', '.'));
const N: number = parseInt(readline());
let defibs = [];
for (let i = 0; i < N; i++) {
    const DEFIB: string = readline();
    let defibSplit = DEFIB.split(';');
    defibs.push({
        name: defibSplit[1],
        longtitude: parseFloat(defibSplit[4].replace(',', '.')),
        latitude: parseFloat(defibSplit[5].replace(',', '.')),
    });
}

function calcX(longA: number, longB: number, latA: number, latB: number): number {
    return (longB - longA) * Math.cos((latA + latB) / 2);
}

function calcY(latA: number, latB: number): number {
    return latB - latA;
}

function d(lon: number, lat: number, defib: {longtitude: number, latitude: number}): number {
    let x = calcX(defib.longtitude, lon, defib.latitude, lat);
    let y = calcY(defib.latitude, lat);
    return Math.sqrt(x * x + y * y) * 6371;
}

let minDefib = defibs.reduce((prev, current) => {
    return d(LON, LAT, prev) < d(LON, LAT, current) ? prev : current;
});

console.log(minDefib.name)
