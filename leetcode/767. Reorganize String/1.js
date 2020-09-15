/**
 * Complexity (n = input string length, k = alphabet size)
 * Time complexity: O(n + k*logk)
 * Space complexity: O(n)
*/
var reorganizeString = function ( S ) {
    let letters = {};
    for ( let char of S ) {
        letters[char] = ( letters[char] || 0 ) + 1;
    }

    let letterCounts = [];
    for ( let letter of Object.keys( letters ) ) {
        letterCounts.push( [letter, letters[letter]] );
    }
    letterCounts.sort( ( a, b ) => b[1] - a[1] );

    // Quick check if rearangement is possible or not
    if ( letterCounts[0][1] * 2 - 1 > S.length ) {
        return "";
    }

    // Fill all even-index positions
    let reorganized = [];
    for ( let i = 0; i < S.length; i += 2 ) {
        reorganized[i] = letterCounts[0][0];
        letterCounts[0][1] -= 1;
        if ( letterCounts[0][1] <= 0 ) {
            letterCounts.shift();
        }
    }

    // Fill all odd-index positions
    for ( let i = 1; i < S.length; i += 2 ) {
        reorganized[i] = letterCounts[0][0];
        letterCounts[0][1] -= 1;
        if ( letterCounts[0][1] <= 0 ) {
            letterCounts.shift();
        }
    }

    return reorganized.join( '' );
};
