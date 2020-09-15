/**
 * Complexity (n = input string 1 length, k = input string 2 length)
 * Time complexity: O(max(n,k))
 * Space complexity: O(max(n,k))
 */
var addBinary = function ( a, b ) {
    let carry = 0;
    let result = [];
    for ( let i = 0; i < Math.max( a.length, b.length ); i++ ) {
        if ( i < a.length ) {
            carry += parseInt( a[a.length - i - 1] );
        }
        if ( i < b.length ) {
            carry += parseInt( b[b.length - i - 1] );
        }

        result.push( carry & 1 ? "1" : "0" );
        carry = carry & ( 1 << 1 ) ? 1 : 0;
    }

    if ( carry === 1 ) {
        result.push( "1" );
    }

    return result.reverse().join( '' );
};
