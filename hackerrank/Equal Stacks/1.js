'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = items in stack 1, m = items in stack 2, k = items in stack 3)
 * Time complexity: O(n + m + k)
 * Space complexity: O(n + m + k)
 */
function equalStacks( h1, h2, h3 ) {
    let s1 = makeStack( h1 );
    let s2 = makeStack( h2 );
    let s3 = makeStack( h3 );
    while ( s1.sum !== s2.sum || s2.sum !== s3.sum || s1.sum !== s3.sum ) {
        if ( s1.sum >= s2.sum && s1.sum >= s3.sum ) {
            let removed = s1.stack.pop();
            s1.sum -= removed;
        } else if ( s2.sum >= s1.sum && s2.sum >= s3.sum ) {
            let removed = s2.stack.pop();
            s2.sum -= removed;
        } else if ( s3.sum >= s1.sum && s3.sum >= s2.sum ) {
            let removed = s3.stack.pop();
            s3.sum -= removed;
        }
    }

    return s1.sum;
}

function makeStack( reversedStack ) {
    let stack = [];
    let sum = 0;
    for ( let i = reversedStack.length - 1; i >= 0; i-- ) {
        stack.push( reversedStack[i] );
        sum += reversedStack[i];
    }

    return {
        stack: stack,
        sum: sum
    };
}

function top( stack ) {
    return stack[stack.length - 1];
}

process.stdin.resume();
process.stdin.setEncoding( 'utf-8' );

let inputString = '';
let currentLine = 0;

process.stdin.on( 'data', inputStdin => {
    inputString += inputStdin;
} );

process.stdin.on( 'end', _ => {
    inputString = inputString.trim().split( '\n' ).map( str => str.trim() );

    main();
} );

function readLine() {
    return inputString[currentLine++];
}

function main() {
    const ws = fs.createWriteStream( process.env.OUTPUT_PATH );
    const n1N2N3 = readLine().split( ' ' );
    const n1 = parseInt( n1N2N3[0], 10 );
    const n2 = parseInt( n1N2N3[1], 10 );
    const n3 = parseInt( n1N2N3[2], 10 );
    const h1 = readLine().split( ' ' ).map( h1Temp => parseInt( h1Temp, 10 ) );
    const h2 = readLine().split( ' ' ).map( h2Temp => parseInt( h2Temp, 10 ) );
    const h3 = readLine().split( ' ' ).map( h3Temp => parseInt( h3Temp, 10 ) );
    let result = equalStacks( h1, h2, h3 );
    ws.write( result + "\n" );
    ws.end();
}
