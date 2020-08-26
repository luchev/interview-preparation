/**
 * Complexity (n = number of strings in array, k = average string length)
 * Time complexity: O(n * k)
 * Space complexity: O(k)
 */
var longestCommonPrefix = function ( strs ) {
    if ( strs.length === 0 ) {
        return "";
    } else if ( strs.length === 1 ) {
        return strs[0];
    }

    let prefix = findPrefix( strs[0], strs[1] );

    for ( let i = 2; i < strs.length; i++ ) {
        prefix = findPrefix( prefix, strs[i] );
        if ( prefix === "" ) {
            return "";
        }
    }

    return prefix;
};

function findPrefix( str1, str2 ) {
    let prefix = "";

    for ( let i = 0; i < Math.min( str1.length, str2.length ); i++ ) {
        if ( str1[i] === str2[i] ) {
            prefix += str1[i];
        } else {
            break;
        }
    }

    return prefix;
}
