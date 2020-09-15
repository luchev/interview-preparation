/**
 * Complexity (n = input number)
 * Time complexity: O(logn) - for the number of digits
 * Space complexity: O(logn)
 */
var reverse = function ( x ) {
    let isNegative = x < 0;

    let xStr = x.toString();
    if ( isNegative ) {
        xStr = xStr.substr( 1 );
    }

    xStr = xStr.split( '' ).reverse().join( '' );

    let xReversed = parseInt( xStr );
    if ( isNegative ) {
        xReversed *= -1;
    }

    if ( xReversed < -2147483648 || xReversed > 2147483647 ) {
        return 0;
    }

    return xReversed;
};
