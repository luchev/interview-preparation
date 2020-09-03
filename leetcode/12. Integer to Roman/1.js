/**
 * Complexity (n = input number, k = number of roman symbols)
 * Time complexity: O(k * log k)
 * Space complexity: O(k)
*/
var intToRoman = function ( num ) {
    let mapping = [['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000], ['IV', 4], ['IX', 9], ['XL', 40], ['XC', 90], ['CD', 400], ['CM', 900]];
    mapping.sort( ( a, b ) => b[1] - a[1] );

    let output = "";
    let mappingIndex = 0;
    while ( num > 0 ) {
        if ( mapping[mappingIndex][1] > num ) {
            mappingIndex++;
        } else {
            output += mapping[mappingIndex][0];
            num -= mapping[mappingIndex][1];
        }
    }

    return output;
};
