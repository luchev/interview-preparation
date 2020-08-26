/**
 * Complexity (n = number of strings in array, k = average string length)
 * Time complexity: O(n * k)
 * Space complexity: O(k)
 */
var longestCommonPrefix = function ( strs ) {
    if ( strs.length === 0 ) {
        return "";
    }

    let prefix = "";

    for ( let charIndex = 0; charIndex < strs[0].length; charIndex++ ) {
        let char = strs[0][charIndex];

        let isPrefix = true;
        for ( let strIndex = 1; strIndex < strs.length; strIndex++ ) {
            if ( strs[strIndex][charIndex] !== char ) {
                isPrefix = false;
                break;
            }
        }

        if ( isPrefix ) {
            prefix += char;
        } else {
            break;
        }
    }

    return prefix;
};
