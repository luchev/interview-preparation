'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = string length)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
function alternatingCharacters( s ) {
    let switchLetters = 1;
    for ( let i = 1; i < s.length; i++ ) {
        if ( s[i] !== s[i - 1] ) {
            switchLetters++;
        }
    }
    return s.length - switchLetters;
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
        let result = alternatingCharacters( s );
        ws.write( result + "\n" );
    }
    ws.end();
}
