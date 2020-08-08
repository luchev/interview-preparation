'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = rows, m = columns)
 * Time complexity: O(n * m)
 * Space complexity: O(n * m)
 * Because the input matrix is always 6x6 we can say that Time and Space complexity is O(1) 
 */
function hourglassSum( arr ) {
    let maxSum;
    for ( let row = 1; row < arr.length - 1; row++ ) {
        for ( let col = 1; col < arr[row].length - 1; col++ ) {
            let nextHourglassSum = calculateHourglass( arr, row, col )
            if ( nextHourglassSum > maxSum || maxSum === undefined ) {
                maxSum = nextHourglassSum;
            }
        }
    }
    return maxSum;
}

function calculateHourglass( arr, row, col ) {
    let sum = arr[row][col];
    for ( let i = col - 1; i < col + 2; i++ ) {
        sum += arr[row - 1][i];
    }
    for ( let i = col - 1; i < col + 2; i++ ) {
        sum += arr[row + 1][i];
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

    let arr = Array( 6 );

    for ( let i = 0; i < 6; i++ ) {
        arr[i] = readLine().split( ' ' ).map( arrTemp => parseInt( arrTemp, 10 ) );
    }

    let result = hourglassSum( arr );

    ws.write( result + "\n" );

    ws.end();
}
