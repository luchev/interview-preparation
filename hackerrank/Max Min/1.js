'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = array length)
 * Time complexity: O(n * log(n))
 * Space complexity: O(1)
 */
function maxMin( k, arr ) {
    arr.sort( ( a, b ) => a - b );
    let start = 0;
    let end = k - 1;
    let bestFairness = arr[end] - arr[start];

    while ( end < arr.length ) {
        bestFairness = Math.min( bestFairness, arr[end] - arr[start] );
        start++;
        end++;
    }

    return bestFairness;
}

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
    const n = parseInt( readLine(), 10 );
    const k = parseInt( readLine(), 10 );
    let arr = [];
    for ( let i = 0; i < n; i++ ) {
        const arrItem = parseInt( readLine(), 10 );
        arr.push( arrItem );
    }
    const result = maxMin( k, arr );
    ws.write( result + '\n' );
    ws.end();
}
