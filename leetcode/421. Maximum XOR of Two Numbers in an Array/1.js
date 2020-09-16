/**
 * Complexity (n = input array size)
 * Time complexity: O(n^2)
 * Space complexity: O(1)
 */
var findMaximumXOR = function ( nums ) {
    let best = 0;
    for ( let i = 0; i < nums.length; i++ ) {
        for ( let k = 0; k < nums.length; k++ ) {
            best = Math.max( best, nums[i] ^ nums[k] );
        }
    }
    return best;
};
