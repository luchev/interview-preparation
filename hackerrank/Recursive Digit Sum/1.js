'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = starting number, k = how many times to concatinate n)
 * Time complexity: O(log(n) * K)
 * Space complexity: O(log(n) * k) = O(digits in N * K)
 */
function superDigit( n, k ) {
    let nSum = calcDigitSum( n );
    let queue = [];
    for ( let i = 0; i < k; i++ ) {
        queue.push( nSum );
    }
    while ( queue.length > 1 || queue[0] >= 10 ) {
        let current = queue.shift();
        let sum = calcDigitSum( current );
        if ( queue.length > 0 ) {
            let next = queue.shift();
            sum += calcDigitSum( next );
        }
        queue.push( parseInt( sum ) );
    }
    return queue[0];
}

function calcDigitSum( num ) {
    let sum = 0;
    for ( let c of num.toString() ) {
        sum += parseInt( c.charCodeAt( 0 ) - '0'.charCodeAt( 0 ) );
    }
    return sum;
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
    const nk = readLine().split( ' ' );
    const n = nk[0];
    const k = parseInt( nk[1], 10 );
    const result = superDigit( n, k );
    ws.write( result + '\n' );
    ws.end();
}
