'use strict';

/**
 * Complexity (n = array length)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
function leftShift( arr, shift ) {
    let output = ''
    for ( let i = 0; i < arr.length; i++ ) {
        let shiftedPosition = ( i + shift ) % arr.length
        output = output.concat( arr[shiftedPosition], ' ' )
    }
    return output;
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
    const nd = readLine().split( ' ' );
    const n = parseInt( nd[0], 10 );
    const d = parseInt( nd[1], 10 );
    const a = readLine().split( ' ' ).map( aTemp => parseInt( aTemp, 10 ) );
    console.log( leftShift( a, d ) )
}
