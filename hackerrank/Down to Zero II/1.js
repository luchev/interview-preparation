'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = MAX input number)
 * Time complexity: O(n * log(n))
 * Space complexity: O(n)
 */
function downToZero( n ) {
    return precomputed[n];
}

let max = 1000001

let precomputed = [];
for ( let i = 0; i < 4; i++ ) {
    precomputed.push( i );
}

for ( let i = 2; i < max; i++ ) {
    if ( !precomputed[i] ) {
        precomputed[i] = precomputed[i - 1] + 1;
    }

    precomputed[i] = Math.min( precomputed[i], precomputed[i - 1] + 1 );

    for ( let k = 2; k <= i; k++ ) {
        let ik = i * k;
        if ( ik > max ) {
            break;
        }

        if ( !precomputed[ik] || precomputed[ik] > precomputed[i] ) {
            precomputed[ik] = precomputed[i] + 1;
        }
    }
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
    const q = parseInt( readLine(), 10 );
    for ( let qItr = 0; qItr < q; qItr++ ) {
        const n = parseInt( readLine(), 10 );
        let result = downToZero( n );
        ws.write( result + "\n" );
    }
    ws.end();
}
