const MESSAGE: string = readline();

let bits = '';
for (let char of MESSAGE) {
    let characterBits = char.charCodeAt(0).toString(2);
    if (characterBits.length < 7) {
        characterBits = '0'.repeat(7 - characterBits.length).concat(characterBits);
    }
    bits = bits.concat(characterBits);
}

let output = '';
let currentValue = bits[0];
let currentCount = 1;
for (let i = 1; i < bits.length; i++) {
    if (bits[i] !== currentValue) {
        if (currentValue === '1') {
            output = output.concat('0 ');
        } else {
            output = output.concat('00 ');
        }
        output = output.concat('0'.repeat(currentCount), ' ');
        currentValue = bits[i];
        currentCount = 1;
    } else {
        currentCount++;
    }
}

if (currentValue === '1') {
    output = output.concat('0 ');
} else {
    output = output.concat('00 ');
}
output = output.concat('0'.repeat(currentCount));

console.log(output)
