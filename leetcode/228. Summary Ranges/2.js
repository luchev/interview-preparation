/**
 * Complexity (n = input array size)
 * Time complexity: O(n)
 * Space complexity: O(1) not accounting the output array
 */
var summaryRanges = function ( nums ) {
    if ( nums.length === 0 ) {
        return [];
    }

    let output = [];
    let intervals = [[nums[0], nums[0]]];
    for ( let i = 1; i < nums.length; i++ ) {
        if ( nums[i] == intervals[intervals.length - 1][1] + 1 ) {
            intervals[intervals.length - 1][1] = nums[i];
        } else {
            if ( intervals[intervals.length - 1][0] === intervals[intervals.length - 1][1] ) {
                output.push( intervals[intervals.length - 1][0].toString() );
            } else {
                output.push( intervals[intervals.length - 1][0].toString() + "->" + intervals[intervals.length - 1][1].toString() );
            }
            intervals.push( [nums[i], nums[i]] );
        }
    }

    if ( intervals[intervals.length - 1][0] === intervals[intervals.length - 1][1] ) {
        output.push( intervals[intervals.length - 1][0].toString() );
    } else {
        output.push( intervals[intervals.length - 1][0].toString() + "->" + intervals[intervals.length - 1][1].toString() );
    }

    return output;
};
