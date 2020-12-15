/**
 * Complexity (n = queries, m = MAX editor content length)
 * Time complexity: O(n * m)
 * Space complexity: O(n * m)
 * Very space inefficient, for better space usage we can encode the operations
 * in a way that they are reversible and keep a stack of these encoded operations
 * Then the space will be O(n + m)
 */
function processData( input ) {
    let lines = input.split( '\n' );
    let str = '';
    let undoStack = [];
    undoStack.push( str );
    for ( let i = 1; i < lines.length; i++ ) {
        let split = lines[i].split( ' ' );
        if ( split[0] === '1' ) { // append
            undoStack.push( str );
            str += split[1];
        } else if ( split[0] === '2' ) { // delete
            undoStack.push( str );
            let deleteCharacters = parseInt( split[1] );
            str = str.substr( 0, str.length - deleteCharacters );
        } else if ( split[0] === '3' ) { // print
            console.error( str );
            let index = parseInt( split[1] );
            console.log( str[index - 1] );
        } else if ( split[0] === '4' ) { // undo
            if ( undoStack.length > 0 ) {
                str = undoStack.pop();
            }
        }
    }
}

process.stdin.resume();
process.stdin.setEncoding( "ascii" );
_input = "";
process.stdin.on( "data", function ( input ) {
    _input += input;
} );

process.stdin.on( "end", function () {
    processData( _input );
} );
