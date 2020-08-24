/**
 * Complexity (n = length of input string)
 * Time complexity: O(n)
 * Space complexity: O(n)
*/
var romanToInt = function ( s ) {
    let romanToInt = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        ',': 4, // IV
        '.': 9, // IX
        '/': 40, // XL
        '[': 90, // XC
        ']': 400, // CD
        '-': 900, // CM
    }

    // Special symbols mapping for some romans
    let romanToShortcut = {
        'IV': ',',
        'IX': '.',
        'XL': '/',
        'XC': '[',
        'CD': ']',
        'CM': '-',
    }

    for ( let roman of Object.keys( romanToShortcut ) ) {
        console.log( roman );
        s = s.replace( RegExp( roman, 'g' ), romanToShortcut[roman] );
    }

    let numbers = s.split( '' ).map( x => romanToInt[x] );

    return numbers.reduce( ( agg, item ) => agg + item, 0 );
};
