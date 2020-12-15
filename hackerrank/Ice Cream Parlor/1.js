'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = input array length)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
function icecreamParlor( m, arr ) {
    let set = {};
    for ( let i in arr ) {
        if ( set[arr[i]] === undefined ) {
            set[arr[i]] = [];
        }
        set[arr[i]].push( parseInt( i ) + 1 );
    }
    // console.log(set);
    for ( let i in arr ) {
        let addition = m - arr[i];
        if ( addition === arr[i] ) {
            if ( set[addition] && set[addition].length >= 2 ) {
                return [set[addition][0], set[addition][1]];
            }
        } else {
            if ( set[addition] ) {
                return [Math.min( set[addition][0], set[arr[i]][0] ), Math.max( set[addition][0], set[arr[i]][0] )];
            }
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
        const m = parseInt( readLine(), 10 );
        const n = parseInt( readLine(), 10 );
        const arr = readLine().split( ' ' ).map( arrTemp => parseInt( arrTemp, 10 ) );
        let result = icecreamParlor( m, arr );
        ws.write( result.join( " " ) + "\n" );
    }
    ws.end();
}
