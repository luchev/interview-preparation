/**
 * Complexity (n = number of strings, k = average string length)
 * Time complexity: O(n * k * ALPHABET_SIZE)
 * Space complexity: O(n * k)
 */
var groupAnagrams = function ( strs ) {
    let anagramsMap = {};
    for ( let str of strs ) {
        let strSorted = str.split( '' );
        strSorted.sort();
        strSorted = strSorted.join( '' );

        if ( !anagramsMap[strSorted] ) {
            anagramsMap[strSorted] = [];
        }
        anagramsMap[strSorted].push( str );
    }

    return Object.values( anagramsMap );
};
