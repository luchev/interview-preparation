/**
 * Complexity (n = input string 1 length, k = input string 2 length)
 * Time complexity: O(max(n,k))
 * Space complexity: O(max(n,k))
 */
var addBinary = function ( a, b ) {
    let carry = 0;
    let resultReversed = [];
    for ( let i = 0; i < Math.min( a.length, b.length ); i++ ) {
        carry += parseInt( a[a.length - i - 1] ) + parseInt( b[b.length - i - 1] );
        if ( carry === 0 ) {
            resultReversed.push( "0" );
            carry = 0;
        } else if ( carry === 1 ) {
            resultReversed.push( "1" );
            carry = 0;
        } else if ( carry === 2 ) {
            resultReversed.push( "0" );
            carry = 1;
        } else if ( carry === 3 ) {
            resultReversed.push( "1" );
            carry = 1;
        }
    }

    let longerNumber = a;
    if ( b.length > a.length ) {
        longerNumber = b;
    }

    for ( let i = Math.min( a.length, b.length ); i < longerNumber.length; i++ ) {
        carry += parseInt( longerNumber[longerNumber.length - i - 1] );
        if ( carry === 0 ) {
            resultReversed.push( "0" );
            carry = 0;
        } else if ( carry === 1 ) {
            resultReversed.push( "1" );
            carry = 0;
        } else if ( carry === 2 ) {
            resultReversed.push( "0" );
            carry = 1;
        }
    }

    if ( carry === 1 ) {
        resultReversed.push( "1" );
    }

    return resultReversed.reverse().join( '' );
};
