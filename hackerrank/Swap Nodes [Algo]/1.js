'use strict';
const fs = require( 'fs' );

/**
 * Complexity (n = nodes in the tree)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
function swapNodes( indexes, queries ) {
    let results = [];
    for ( let swapLevel of queries ) {
        swapRecursive( indexes, swapLevel, 0, 1 );
        let traversal = [];
        traverse( indexes, 0, traversal );
        results.push( traversal );
    }
    return results;
}

function swapRecursive( tree, swapK, currentNode, level ) {
    if ( !tree[currentNode] ) {
        return;
    }
    if ( level % swapK === 0 ) {
        [tree[currentNode][0], tree[currentNode][1]] = [tree[currentNode][1], tree[currentNode][0]]
    }
    swapRecursive( tree, swapK, tree[currentNode][0] - 1, level + 1 );
    swapRecursive( tree, swapK, tree[currentNode][1] - 1, level + 1 );
}

function traverse( tree, currentNode, result ) {
    if ( !tree[currentNode] ) {
        return;
    }
    traverse( tree, tree[currentNode][0] - 1, result );
    result.push( currentNode + 1 );
    traverse( tree, tree[currentNode][1] - 1, result );
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
    const n = parseInt( readLine(), 10 );
    let indexes = Array( n );
    for ( let indexesRowItr = 0; indexesRowItr < n; indexesRowItr++ ) {
        indexes[indexesRowItr] = readLine().split( ' ' ).map( indexesTemp => parseInt( indexesTemp, 10 ) );
    }
    const queriesCount = parseInt( readLine(), 10 );
    let queries = [];
    for ( let queriesItr = 0; queriesItr < queriesCount; queriesItr++ ) {
        const queriesItem = parseInt( readLine(), 10 );
        queries.push( queriesItem );
    }
    let result = swapNodes( indexes, queries );
    ws.write( result.map( x => x.join( ' ' ) ).join( "\n" ) + "\n" );
    ws.end();
}
