'use strict';
const fs = require( 'fs' );

/**
 * Complexity (X = number, N = power)
 * Time complexity: O(X * log(N))
 * Space complexity: O(X), but much better in reality
 * Time complexity comes from
 * - sqrt(X) for each loop inside powerSum
 * - sqrt(X) for powerSumRecursive, which should quickly converge
 * - log(N) for the Math.pow()
 */
function powerSum( X, N ) {
    let powers = [];
    for ( let i = 0; i < Math.sqrt( X ) + 1; i++ ) {
        powers[i] = Math.pow( i, N );
    }

    let combinations = 0;
    for ( let i = 1; i < powers.length; i++ ) {
        if ( powers[i] === X ) {
            combinations++;
        } else if ( powers[i] < X ) {
            combinations += powerSumRecursive( X, N, powers, [i], powers[i] );
        } else {
            break;
        }
    }

    return combinations;
}

function powerSumRecursive( X, N, powers, numbers, value ) {
    let combinations = 0;
    for ( let i = numbers[numbers.length - 1] + 1; i < powers.length; i++ ) {
        if ( value + powers[i] === X ) {
            combinations++;
        } else if ( value + powers[i] < X ) {
            combinations += powerSumRecursive( X, N, powers, powers.concat( [i] ), value + powers[i] );
        } else {
            break;
        }
    }
    return combinations
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
    const X = parseInt( readLine(), 10 );
    const N = parseInt( readLine(), 10 );
    let result = powerSum( X, N );
    ws.write( result + "\n" );
    ws.end();
}
