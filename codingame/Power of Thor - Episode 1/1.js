var inputs = readline().split( ' ' );
const lightX = parseInt( inputs[0] ); // the X position of the light of power
const lightY = parseInt( inputs[1] ); // the Y position of the light of power
const initialTx = parseInt( inputs[2] ); // Thor's starting X position
const initialTy = parseInt( inputs[3] ); // Thor's starting Y position
let tx = initialTx;
let ty = initialTy;

// game loop
while ( true ) {
    const remainingTurns = parseInt( readline() ); // The remaining amount of turns Thor can move. Do not remove this line.
    let direction = '';

    if ( ty < lightY ) {
        direction = 'S';
        ty += 1;
    } else if ( ty > lightY ) {
        direction = 'N';
        ty -= 1;
    }

    if ( tx < lightX ) {
        direction = direction.concat( 'E' );
        tx += 1;
    } else if ( tx > lightX ) {
        direction = direction.concat( 'W' );
        tx -= 1;
    }

    console.log( direction );
}
