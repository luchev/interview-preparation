/**
 * Complexity (n = length of num1, k = length of num2)
 * Time complexity: O(n + m)
 * Space complexity: O( max(n, m) )
 */
var addStrings = function ( num1, num2 ) {
    let carry = 0;
    let result = "";

    for ( let i = 0; i < Math.max( num1.length, num2.length ); i++ ) {
        let num1Index = num1.length - i - 1;
        let num2Index = num2.length - i - 1;

        if ( num1Index >= 0 ) {
            carry += parseInt( num1[num1Index] );
        }
        if ( num2Index >= 0 ) {
            carry += parseInt( num2[num2Index] );
        }

        result = ( carry % 10 ).toString() + result;
        carry = Math.floor( carry / 10 );
    }

    if ( carry === 1 ) {
        result = '1' + result;
    }

    return result;
};
