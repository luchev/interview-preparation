'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = string length)
 * Time complexity: O(n)
 * Space complexity: O(number of letters in the alphabet)
 */
function stringConstruction( s ) {
    let letters = {};
    for ( let c of s ) {
        letters[c] = 1;
    }
    return Object.keys( letters ).length;
}

process.stdin.resume();
process.stdin.setEncoding( 'utf-8' );

let inputString = '';
let currentLine = 0;

process.stdin.on( 'data', inputStdin => {
    inputString += inputStdin;
} );

process.stdin.on( 'end', _ => {
    inputString = inputString.replace( /\s*$/, '' )
        .split( '\n' )
        .map( str => str.replace( /\s*$/, '' ) );

    main();
} );

function readLine() {
    return inputString[currentLine++];
}

function main() {
    const ws = fs.createWriteStream( process.env.OUTPUT_PATH );
    const q = parseInt( readLine(), 10 );
    for ( let qItr = 0; qItr < q; qItr++ ) {
        const s = readLine();
        let result = stringConstruction( s );
        ws.write( result + "\n" );
    }
    ws.end();
}
