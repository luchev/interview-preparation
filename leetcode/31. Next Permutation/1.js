/**
 * Complexity (n = input array size)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var nextPermutation = function ( nums ) {
    let firstDecreasing = -1;
    for ( let i = nums.length - 2; i >= 0; i-- ) {
        if ( nums[i] < nums[i + 1] ) {
            firstDecreasing = i;
            break;
        }
    }
    if ( firstDecreasing === -1 ) {
        return nums.reverse();
    }

    let rightLarger = -1;
    for ( let i = nums.length - 1; i > firstDecreasing; i-- ) {
        if ( nums[i] > nums[firstDecreasing] ) {
            rightLarger = i;
            break;
        }
    }

    [nums[firstDecreasing], nums[rightLarger]] = [nums[rightLarger], nums[firstDecreasing]]

    let reversedTail = nums.splice( firstDecreasing + 1, nums.length ).reverse();
    nums.push( ...reversedTail );
};
