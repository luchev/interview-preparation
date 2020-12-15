'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = input string length)
 * Time complexity: O(n^2)
 * Space complexity: O(n^2)
 */
function sherlockAndAnagrams( s ) {
    let anagrams = 0;

    for ( let length = 1; length <= s.length - 1; length++ ) {
        
        let subSetMap = {};
        let currentCharacters = {};
        for ( let i = 0; i < length; i++ ) {
            currentCharacters[s[i]] = ( currentCharacters[s[i]] || 0 ) + 1;
        }
        subSetMap[JSON.stringify( currentCharacters )] = 1;
        
        for ( let lastChar = length; lastChar < s.length; lastChar++ ) {
            currentCharacters[s[lastChar - length]] -= 1;
            currentCharacters[s[lastChar]] = ( currentCharacters[s[lastChar]] || 0 ) + 1;
            if ( currentCharacters[s[lastChar - length]] === 0 ) {
                currentCharacters[s[lastChar - length]] = undefined;
            }
            
            if ( subSetMap[JSON.stringify( currentCharacters )] ) {
                anagrams += subSetMap[JSON.stringify( currentCharacters )];
                subSetMap[JSON.stringify( currentCharacters )] += 1;
            } else {
                subSetMap[JSON.stringify( currentCharacters )] = 1;
            }
        }
    }

    return anagrams;
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
    const q = parseInt( readLine(), 10 );
    for ( let qItr = 0; qItr < q; qItr++ ) {
        const s = readLine();
        let result = sherlockAndAnagrams( s );
        ws.write( result + "\n" );
    }
    ws.end();
}
