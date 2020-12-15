'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = array length)
 * Time complexity: O(n)
 * Space complexity: O(1)
 * We use space for the hash map but our alphabet is limited hence O(1) space
 */
function minimumDistances( a ) {
    let indices = {}
    let minDistance = a.length;
    for ( let i = 0; i < a.length; i++ ) {
        if ( indices[a[i]] !== undefined ) {
            if ( i - indices[a[i]] < minDistance ) {
                minDistance = i - indices[a[i]]
            }
        } else {
            indices[a[i]] = i;
        }
    }

    if ( minDistance === a.length ) {
        return -1;
    }
    return minDistance;
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
    const a = readLine().split( ' ' ).map( aTemp => parseInt( aTemp, 10 ) );
    let result = minimumDistances( a );
    ws.write( result + "\n" );
    ws.end();
}
