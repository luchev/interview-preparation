/**
 * Complexity (n = length of numbers list)
 * Time complexity: O(n^2)
 * Space complexity: O(n) this excludes the space for the output array
 */
var threeSum = function ( nums ) {
    nums.sort( ( a, b ) => a - b );

    let solutions = [];

    for ( let i = 0; i < nums.length; i++ ) {
        if ( nums[i] != nums[i - 1] ) {
            let left = i + 1;
            let right = nums.length - 1;
            while ( left < right ) {
                let currentSum = nums[i] + nums[left] + nums[right];
                if ( currentSum === 0 ) {
                    if ( solutions.length === 0 ||
                        solutions.length > 0 && (
                            solutions[solutions.length - 1][2] !== nums[right] ||
                            solutions[solutions.length - 1][1] !== nums[left]
                        ) ) {
                        solutions.push( [nums[i], nums[left], nums[right]] );
                    }
                    right--;
                } else if ( currentSum > 0 ) {
                    right--;
                } else {
                    left++;
                }
            }
        }
    }

    return solutions;
};
