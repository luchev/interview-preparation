'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = length of input string)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
function isBalanced( s ) {
    let stack = [];
    let openBrackets = new Set( ['{', '[', '('] );

    for ( let char of s ) {
        if ( openBrackets.has( char ) ) {
            stack.push( char );
        } else {
            if ( stack.length === 0 ) {
                return 'NO';
            }
            let top = stack.pop();
            if ( char === ')' ) {
                if ( top !== '(' ) {
                    return 'NO';
                }
            }
            if ( char === ']' ) {
                if ( top !== '[' ) {
                    return 'NO';
                }
            }
            if ( char === '}' ) {
                if ( top !== '{' ) {
                    return 'NO';
                }
            }
        }
    }
    if ( stack.length !== 0 ) {
        return 'NO';
    }
    return 'YES';
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
        const s = readLine();
        let result = isBalanced( s );
        ws.write( result + "\n" );
    }
    ws.end();
}
