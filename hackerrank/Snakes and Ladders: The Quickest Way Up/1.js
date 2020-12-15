'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = board size (always 100), s = snakes, d = ladders)
 * Time complexity: O(n + s + d)
 * Space complexity: O(n + s + d)
 */
function quickestWayUp( ladders, snakes ) {
    let shortcuts = {};
    for ( let ladder of ladders ) {
        shortcuts[ladder[0]] = ladder[1];
    }
    for ( let snake of snakes ) {
        shortcuts[snake[0]] = snake[1];
    }

    let visited = new Set();

    let queue = [[1, 0]];
    while ( queue.length > 0 ) {
        let current = queue.shift();
        let currentVertex = current[0];
        let currentTurns = current[1];

        if ( currentVertex === 100 ) {
            return currentTurns;
        }

        if ( visited.has( currentVertex ) ) {
            continue;
        }
        visited.add( currentVertex );

        for ( let i = currentVertex + 1; i <= currentVertex + 6; i++ ) {
            if ( shortcuts[i] ) {
                queue.push( [shortcuts[i], currentTurns + 1] );
            } else {
                queue.push( [i, currentTurns + 1] );
            }
        }
    }
    return -1;
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
        let ladders = Array( n );
        for ( let i = 0; i < n; i++ ) {
            ladders[i] = readLine().split( ' ' ).map( laddersTemp => parseInt( laddersTemp, 10 ) );
        }
        const m = parseInt( readLine(), 10 );
        let snakes = Array( m );
        for ( let i = 0; i < m; i++ ) {
            snakes[i] = readLine().split( ' ' ).map( snakesTemp => parseInt( snakesTemp, 10 ) );
        }
        let result = quickestWayUp( ladders, snakes );
        ws.write( result + "\n" );
    }
    ws.end();
}
