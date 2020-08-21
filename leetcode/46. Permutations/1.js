/**
 * Complexity (n = input array size)
 * Time complexity: O(n * n!)
 * Space complexity: O(n!)
 */
var permute = function ( nums ) {
    let permutations = [];
    permuteRecursive( nums, permutations, 0 );
    return permutations;
};

function permuteRecursive( numbers, permutations, from ) {
    if ( from === numbers.length - 1 ) {
        // Make a copy of the array, otherwise it will be a reference to the original
        permutations.push( Array.from( numbers ) );
        return;
    }

    for ( let i = from; i <= numbers.length - 1; i++ ) {
        [numbers[from], numbers[i]] = [numbers[i], numbers[from]]
        permuteRecursive( numbers, permutations, from + 1 );
        [numbers[from], numbers[i]] = [numbers[i], numbers[from]]
    }
}
