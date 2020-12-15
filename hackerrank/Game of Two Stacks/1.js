'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = items in stack 1, m = items in stack 2)
 * Time complexity: O(n + m)
 * Space complexity: O(1)
 */
function twoStacks( x, a, b ) {
    let a_i = 0;
    let b_i = 0;
    let a_sum = 0;
    let b_sum = 0;

    for ( a_i = 0; a_i < a.length; a_i++ ) {
        if ( a_sum + a[a_i] > x ) {
            break;
        }
        a_sum += a[a_i];
    }

    for ( b_i = 0; b_i < b.length; b_i++ ) {
        if ( b_sum + a_sum + b[b_i] > x ) {
            break;
        }
        b_sum += b[b_i];
    }

    let max_count = a_i + b_i;
    for ( ; a_i > 0; a_i-- ) {
        a_sum -= a[a_i - 1];
        for ( ; b_i < b.length; b_i++ ) {
            if ( b_sum + a_sum + b[b_i] > x ) {
                break;
            }
            b_sum += b[b_i];
        }
        max_count = Math.max( a_i - 1 + b_i, max_count );
    }
    return max_count;
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
    const g = parseInt( readLine(), 10 );
    for ( let gItr = 0; gItr < g; gItr++ ) {
        const nmx = readLine().split( ' ' );
        const n = parseInt( nmx[0], 10 );
        const m = parseInt( nmx[1], 10 );
        const x = parseInt( nmx[2], 10 );
        const a = readLine().split( ' ' ).map( aTemp => parseInt( aTemp, 10 ) );
        const b = readLine().split( ' ' ).map( bTemp => parseInt( bTemp, 10 ) );
        let result = twoStacks( x, a, b );
        ws.write( result + "\n" );
    }
    ws.end();
}
