/**
 * Complexity (n = number of strings, k = average string length)
 * Time complexity: O(n * k * ALPHABET_SIZE)
 * Space complexity: O(n * k)
 */
var groupAnagrams = function ( strs ) {
    let strings = [];
    for ( let str of strs ) {
        let strSorted = str.split( '' );
        strSorted.sort();
        strSorted = strSorted.join( '' );
        strings.push( [str, strSorted] );
    }

    let anagramsMap = {};
    for ( let tuple of strings ) {
        if ( !anagramsMap[tuple[1]] ) {
            anagramsMap[tuple[1]] = [];
        }
        anagramsMap[tuple[1]].push( tuple[0] );
    }

    return Object.values( anagramsMap );
};
