const operation: string = readline();
const startingShift: number = parseInt(readline()) % 26;
const rotors: string[] = [];
for (let i = 0; i < 3; i++) {
    rotors.push(readline());
}
let message: string = readline();

const A = 'A'.charCodeAt(0);

function applyRotor(rotor: string, input: string): string {
    let result = '';
    for (let char of input) {
        result += rotor[char.charCodeAt(0) - A];
    }
    return result;
}

function applyCaesar(input: string, startingShift: number): string {
    let output = '';
    let shift = startingShift;
    for (let i = 0; i < input.length; i++) {
        let transformed = String.fromCharCode((message.charCodeAt(i) - A + shift) % 26 + A);
        output += transformed;
        shift++;
    }
    return output;
}

function applyCaesarReverse(input: string, endingShift: number): string {
    let output = '';
    let shift = endingShift;
    for (let i = input.length - 1; i >= 0; i--) {
        let transformed = String.fromCharCode((input.charCodeAt(i) - A - shift + 26000) % 26 + A);
        output = transformed + output;
        shift--;
    }
    return output;
}

function applyRotorReverse(rotor: string, input: string): string {
    let result = '';
    let rotorDict = {};
    for (let i = 0; i < rotor.length; i++) {
        rotorDict[rotor[i]] = String.fromCharCode(A + i);
    }
    for (let char of input) {
        result += rotorDict[char];
    }
    return result;
}

if (operation === 'ENCODE') {
    let encrypted = applyCaesar(message, startingShift);
    for (let rotor of rotors) {
        encrypted = applyRotor(rotor, encrypted);
    }
    console.log(encrypted);
} else {
    let decrypted = message;
    for (let i = rotors.length - 1; i >= 0; i--) {
        decrypted = applyRotorReverse(rotors[i], decrypted);
    }
    decrypted = applyCaesarReverse(decrypted, startingShift + decrypted.length - 1);
    console.log(decrypted);
}
