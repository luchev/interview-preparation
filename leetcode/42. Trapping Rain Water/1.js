/**
 * Complexity (n = input array size)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var trap = function ( height ) {
    if ( height.length === 0 ) {
        return 0;
    }

    let waterLevelLeft = [height[0]];
    for ( let i = 1; i < height.length; i++ ) {
        waterLevelLeft.push( Math.max( waterLevelLeft[i - 1], height[i] ) );
    }

    let waterLevelRight = [height[height.length - 1]];
    for ( let i = height.length - 2; i >= 0; i-- ) {
        waterLevelRight.push( Math.max( height[i], waterLevelRight[waterLevelRight.length - 1] ) );
    }
    waterLevelRight.reverse();

    let waterLevel = [];
    for ( let i = 0; i < waterLevelLeft.length; i++ ) {
        waterLevel.push( Math.min( waterLevelLeft[i], waterLevelRight[i] ) );
    }

    let rain = 0;
    for ( let i = 0; i < waterLevel.length; i++ ) {
        rain += waterLevel[i] - height[i];
    }

    return rain;
};
