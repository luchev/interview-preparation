/**
 * Complexity (n = input array size)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var rob = function ( nums ) {
    let bestPrice = 0;
    let prevPrice = 0;
    for ( let i = 0; i < nums.length; i++ ) {
        let bestPriceNew = Math.max( bestPrice, prevPrice + nums[i] );
        prevPrice = bestPrice;
        bestPrice = bestPriceNew;
    }

    return bestPrice;
};
