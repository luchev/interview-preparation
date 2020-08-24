/**
 * Complexity (n = length of numbers list)
 * Time complexity: O(n^2)
 * Space complexity: O(1)
 */
var threeSumClosest = function ( nums, target ) {
    nums.sort( ( a, b ) => a - b );

    let closest = Math.pow( 2, 62 );
    for ( let i = 0; i < nums.length; i++ ) {
        if ( nums[i] !== nums[i - 1] ) {
            let left = i + 1;
            let right = nums.length - 1;

            while ( left < right ) {
                let currentSum = nums[i] + nums[left] + nums[right];
                if ( Math.abs( currentSum - target ) < Math.abs( closest - target ) ) {
                    closest = currentSum;
                }
                
                if ( currentSum < target ) {
                    left++;
                } else {
                    right--;
                }
            }
        }
    }

    return closest;
};
