var inputs = readline().split( ' ' );
const W = parseInt( inputs[0] ); // width of the building.
const H = parseInt( inputs[1] ); // height of the building.
const N = parseInt( readline() ); // maximum number of turns before game over.
var inputs = readline().split( ' ' );
const X0 = parseInt( inputs[0] );
const Y0 = parseInt( inputs[1] );

var x = X0;
var y = Y0;
var up = 0;
var down = H - 1;
var left = 0;
var right = W - 1;

// game loop
while ( true ) {
    const bombDir = readline(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if ( bombDir.includes( 'U' ) ) {
        down = y - 1;
        y = Math.floor( ( up + down ) / 2 );
    } else if ( bombDir.includes( 'D' ) ) {
        up = y + 1;
        y = Math.floor( ( up + down ) / 2 );
    }

    if ( bombDir.includes( 'L' ) ) {
        right = x - 1;
        x = Math.floor( ( left + right ) / 2 );
    } else if ( bombDir.includes( 'R' ) ) {
        left = x + 1;
        x = Math.floor( ( left + right ) / 2 );
    }
    console.log( x, y );
}
