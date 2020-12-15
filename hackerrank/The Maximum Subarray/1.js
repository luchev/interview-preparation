'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = array length)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
function subSequence( arr ) {
    let sum = 0;
    let onlyNegativeNumbers = true;
    for ( let i of arr ) {
        if ( i >= 0 ) {
            sum += i;
            onlyNegativeNumbers = false;
        }
    }

    if ( onlyNegativeNumbers ) {
        return Math.max( ...arr );
    } else {
        return sum;
    }
}

/**
 * Complexity (n = array length)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
function subArray( arr ) {
    let maxSum = arr[0];
    let currentSum = 0;
    for ( let i = 0; i < arr.length; i++ ) {
        if ( currentSum + arr[i] < 0 ) {
            currentSum = 0;
            if ( arr[i] > maxSum ) {
                maxSum = arr[i];
            }
        } else {
            currentSum += arr[i];
            if ( currentSum > maxSum ) {
                maxSum = currentSum;
            }
        }
    }
    return maxSum;
}

function maxSubarray( arr ) {
    return [subArray( arr ), subSequence( arr )]

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
    const t = parseInt( readLine(), 10 );
    for ( let tItr = 0; tItr < t; tItr++ ) {
        const n = parseInt( readLine(), 10 );
        const arr = readLine().split( ' ' ).map( arrTemp => parseInt( arrTemp, 10 ) );
        let result = maxSubarray( arr );
        ws.write( result.join( " " ) + "\n" );
    }
    ws.end();
}
