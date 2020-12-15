'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = string 1 length, m = string 2 length)
 * Time complexity: O(n + m)
 * Space complexity: O(number of letters in the alphabet)
 */
function makingAnagrams( s1, s2 ) {
    let letters = {};

    for ( let c of s1 ) {
        if ( letters[c] !== undefined ) {
            letters[c]++;
        } else {
            letters[c] = 1;
        }
    }
    
    for ( let c of s2 ) {
        if ( letters[c] !== undefined ) {
            letters[c]--;
        } else {
            letters[c] = -1;
        }
    }
    
    let removeLettersCount = 0;
    Object.keys( letters ).forEach( ( letter ) => {
        removeLettersCount += Math.abs( letters[letter] );
    } );
    
    return removeLettersCount;
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
    const s1 = readLine();
    const s2 = readLine();
    let result = makingAnagrams( s1, s2 );
    ws.write( result + "\n" );
    ws.end();
}
