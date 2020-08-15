/**
 * Complexity (n = length of height array)
 * Time complexity: O(n)
 * Space complexity: O(1)
 * Looks suspicious, but works. Check leetcode discussion for more explanations
*/
var maxArea = function ( height ) {
    let left = 0;
    let right = height.length - 1;
    let best = ( right - left ) * Math.min( height[left], height[right] );

    while ( left < right ) {
        if ( height[left] < height[right] ) {
            left++;
        } else {
            right--;
        }

        let newArea = ( right - left ) * Math.min( height[left], height[right] );
        best = Math.max( best, newArea );
    }

    return best;
};
