/**
 * Complexity (n = input array size)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var summaryRanges = function ( nums ) {
    if ( nums.length === 0 ) {
        return [];
    }

    let intervals = [[nums[0], nums[0]]];
    for ( let i = 1; i < nums.length; i++ ) {
        if ( nums[i] == intervals[intervals.length - 1][1] + 1 ) {
            intervals[intervals.length - 1][1] = nums[i];
        } else {
            intervals.push( [nums[i], nums[i]] );
        }
    }

    let output = [];
    for ( let interval of intervals ) {
        if ( interval[0] === interval[1] ) {
            output.push( interval[0].toString() );
        } else {
            output.push( interval[0].toString() + "->" + interval[1].toString() );
        }
    }

    return output;
};

// -5 -4 -3 0 3 4 6 7 8 ==> [ [-5, -3] [0, 0] [3, 4] [6, 8] ]
// [ "-5->-3", "0", "3->4", "6->8" ]
