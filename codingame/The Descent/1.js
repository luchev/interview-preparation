// game loop
while ( true ) {
    let index = 0;
    let height = -1;
    for ( let i = 0; i < 8; i++ ) {
        const h = parseInt( readline() ); // represents the height of one mountain.
        if ( h > height ) {
            height = h;
            index = i;
        }
    }
    console.log( index )
}
