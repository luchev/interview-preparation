/**
 * Complexity (n = input array size)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var rob = function ( nums ) {
    if ( nums.length === 0 ) {
        return 0
    }

    let bestPrice = nums[0];
    let takePrev = true;
    let prevBest = 0;
    for ( let i = 1; i < nums.length; i++ ) {
        if ( takePrev ) {
            if ( prevBest + nums[i] > bestPrice ) {
                let newBestPrice = prevBest + nums[i];
                prevBest = bestPrice;
                bestPrice = newBestPrice;
                takePrev = true;
            } else {
                takePrev = false;
            }
        } else {
            prevBest = bestPrice
            bestPrice = bestPrice + nums[i];
            takePrev = true;
        }
    }

    return bestPrice;
};
