'use strict';
const fs = require( 'fs' );
/**
 * Complexity (n = string length)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
function highestValuePalindrome( s, n, k ) {
    let palindrome = s.split( '' );
    let differentPositions = 0;
    for ( let i = 0; i < Math.floor( n / 2 ); i++ ) {
        if ( s[i] !== s[n - i - 1] ) {
            differentPositions++;
        }
    }
    for ( let i = 0; i < Math.floor( n / 2 ); i++ ) {
        if ( k < 0 ) {
            break;
        }
        if ( k > differentPositions && s[i] !== '9' && s[n - i - 1] !== '9' ) {
            if ( k < 2 ) {
                continue;
            }
            k -= 2;
            palindrome[i] = '9';
            palindrome[n - i - 1] = '9';
            if ( s[i] != s[n - i - 1] ) {
                differentPositions--;
            }
        } else {
            if ( s[i] !== s[n - i - 1] ) {
                if ( s.charCodeAt( i ) < s.charCodeAt( n - i - 1 ) ) {
                    palindrome[i] = s[n - i - 1];
                } else {
                    palindrome[n - i - 1] = s[i];
                }
                k--;
                differentPositions--;
            }
        }
    }
    if ( k >= 1 ) {
        palindrome[Math.floor( n / 2 )] = '9';
    }

    if ( k < 0 ) {
        return "-1";
    } else {
        return palindrome.join( '' );
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
    const nk = readLine().split( ' ' );
    const n = parseInt( nk[0], 10 );
    const k = parseInt( nk[1], 10 );
    const s = readLine();
    let result = highestValuePalindrome( s, n, k );
    ws.write( result + "\n" );
    ws.end();
}
