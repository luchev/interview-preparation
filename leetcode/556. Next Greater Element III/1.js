/**
 * Complexity (n = digits in the input number)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */

var nextGreaterElement = function ( n ) {
    let numSplit = n.toString().split( '' ).map( ( x ) => parseInt( x ) );
    let next = nextPermutation( numSplit )
    if ( next == -1 || next > Math.pow( 2, 31 ) - 1 ) {
        return -1;
    } else {
        return next;
    }
};

var nextPermutation = function ( nums ) {
    let firstDecreasing = -1;
    for ( let i = nums.length - 2; i >= 0; i-- ) {
        if ( nums[i] < nums[i + 1] ) {
            firstDecreasing = i;
            break;
        }
    }
    if ( firstDecreasing === -1 ) {
        return -1;
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
    return parseInt( nums.join( '' ) );
};
