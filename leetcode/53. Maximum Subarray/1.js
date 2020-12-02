/**
 * Complexity (n = array length)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var maxSubArray = function ( nums ) {
    let maxSum = nums[0];
    let currentSum = 0;
    for ( let i = 0; i < nums.length; i++ ) {
        if ( currentSum + nums[i] < 0 ) {
            currentSum = 0;
            if ( nums[i] > maxSum ) {
                maxSum = nums[i];
            }
        } else {
            currentSum += nums[i];
            if ( currentSum > maxSum ) {
                maxSum = currentSum;
            }
        }
    }
    return maxSum;
};
