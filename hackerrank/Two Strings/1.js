'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = length of string 1, m = length of string 2)
 * Time complexity: O(n + m)
 * Space complexity: O(SIZE OF ALPHABET)
 */
function twoStrings( s1, s2 ) {
    let set = {};
    for ( let char of s1 ) {
        set[char] = 1;
    }
    for ( let char of s2 ) {
        if ( set[char] === 1 ) {
            return "YES";
        }
    }
    return "NO";
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
        const s1 = readLine();
        const s2 = readLine();
        let result = twoStrings( s1, s2 );
        ws.write( result + "\n" );
    }
    ws.end();
}
