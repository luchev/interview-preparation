'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = array length, k = number of characters in the alphabet)
 * Time complexity: O(n)
 * Space complexity: O(k)
 */
function equalizeArray( arr ) {
    let countingArr = {}
    for ( let i = 0; i < arr.length; i++ ) {
        if ( countingArr[arr[i]] !== undefined ) {
            countingArr[arr[i]] += 1
        } else {
            countingArr[arr[i]] = 1
        }
    }

    let maxOccurrences = 0
    console.log( countingArr )
    Object.keys( countingArr ).forEach( ( key ) => {
        if ( countingArr[key] > maxOccurrences ) {
            maxOccurrences = countingArr[key]
        }
    } );

    return arr.length - maxOccurrences;
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
    const n = parseInt( readLine(), 10 );
    const arr = readLine().split( ' ' ).map( arrTemp => parseInt( arrTemp, 10 ) );
    let result = equalizeArray( arr );
    ws.write( result + "\n" );
    ws.end();
}
