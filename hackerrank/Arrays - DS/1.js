'use strict';

/**
 * Complexity (n = array length)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
function reverseArray( a ) {
    let reversed = [];
    for ( let i = a.length - 1; i >= 0; i-- ) {
        reversed.push( a[i] )
    }
    return reversed;
}

const fs = require( 'fs' );

process.stdin.resume();
process.stdin.setEncoding( 'utf-8' );

let inputString = '';
let currentLine = 0;

process.stdin.on( 'data', inputStdin => {
    inputString += inputStdin;
} );

process.stdin.on( 'end', function () {
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
    const arrCount = parseInt( readLine(), 10 );
    const arr = readLine().split( ' ' ).map( arrTemp => parseInt( arrTemp, 10 ) );
    const res = reverseArray( arr );
    ws.write( res.join( ' ' ) + '\n' );
    ws.end();
}
