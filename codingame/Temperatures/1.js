const n = parseInt( readline() ); // the number of temperatures to analyse
var inputs = readline().split( ' ' );
var closest = 100000;
for ( let i = 0; i < n; i++ ) {
    const t = parseInt( inputs[i] );// a temperature expressed as an integer ranging from -273 to 5526
    if ( Math.abs( t ) < Math.abs( closest ) ) {
        closest = t;
    } else if ( t === -closest ) {
        closest = Math.abs( t );
    }
}

if ( n == 0 ) {
    console.log( 0 );
} else {
    console.log( closest );
}
