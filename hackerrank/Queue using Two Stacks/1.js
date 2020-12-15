/**
 * Complexity (n = number of queries)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
function processData( input ) {
    let queue = new Queue();
    let lines = input.split( '\n' );
    for ( let i = 1; i < lines.length; i++ ) {
        let op = lines[i].split( ' ' );
        if ( op[0] === '1' ) {
            queue.enqueue( op[1] );
        } else if ( op[0] === '2' ) {
            queue.dequeue();
        } else if ( op[0] === '3' ) {
            console.log( queue.poll() );
        }
    }
}

class Queue {
    constructor() {
        this.s1 = [];
        this.s2 = [];
    }

    enqueue( data ) {
        this.s1.push( data );
    }

    dequeue() {
        if ( this.s2.length === 0 ) {
            while ( this.s1.length !== 0 ) {
                this.s2.push( this.s1.pop() );
            }
        }
        this.s2.pop();
    }

    poll() {
        if ( this.s2.length === 0 ) {
            while ( this.s1.length !== 0 ) {
                this.s2.push( this.s1.pop() );
            }
        }
        return this.s2[this.s2.length - 1];;
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
