interface Light {
    dist: number;
    dur: number;
};

const speed: number = parseInt(readline());
const lightCount: number = parseInt(readline());
let lights: Light[] = [];
for (let i = 0; i < lightCount; i++) {
    var inputs: string[] = readline().split(' ');
    const distance: number = parseInt(inputs[0]);
    const duration: number = parseInt(inputs[1]);
    lights.push({
        dist: distance,
        dur: duration,
    });
}

console.error(lights);

for (let i = speed; i > 0; i--) {
    let mps = i * 1000 / 3600; // meters per second
    let possible = true;
    console.error("Speed ", i, " MPS ", mps);
    for (let light of lights) {
        let time = light.dist / mps;
        if (Math.round(time % (light.dur * 2) * 1000) / 1000 % (light.dur * 2) >= light.dur) {
            console.error();
            possible = false;
            break;
        }
    }
    if (possible) {
        console.log(i);
        break;
    }
}
