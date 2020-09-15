/**
 * Complexity (n = input array size)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var trap = function ( height ) {
    if ( height.length === 0 ) {
        return 0;
    }
    let left = 0;
    let right = height.length - 1;
    let leftMaxHeight = 0;
    let rightMaxHeight = 0;

    let rain = 0;
    while ( left < right ) {
        if ( height[left] < height[right] ) {
            if ( height[left] > leftMaxHeight ) {
                leftMaxHeight = height[left];
            }
            rain += leftMaxHeight - height[left];
            left++;
        } else {
            if ( height[right] > rightMaxHeight ) {
                rightMaxHeight = height[right];
            }
            rain += rightMaxHeight - height[right];
            right--;
        }
    }

    return rain;
};
