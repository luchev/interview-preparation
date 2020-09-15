/**
 * Complexity (n = input array size)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var insert = function ( intervals, newInterval ) {
    if ( intervals === [] ) {
        return [newInterval];
    }

    let insertAfter = -1;
    for ( let i = 0; i < intervals.length; i++ ) {
        if ( intervals[i][0] > newInterval[0] ) {
            break;
        }
        insertAfter = i;
    }

    let merged = [];
    for ( let i = 0; i <= insertAfter; i++ ) {
        merged.push( Array.from( intervals[i] ) );
    }

    if ( merged.length > 0 && newInterval[0] <= merged[merged.length - 1][1] ) {
        // Merge newInterval with closest interval to the left
        merged[merged.length - 1][1] = Math.max( merged[merged.length - 1][1], newInterval[1] );
    } else {
        // Append newInterval
        merged.push( Array.from( newInterval ) );
    }

    // Merge intervals to the right of newInterval with newInterval
    for ( let i = insertAfter + 1; i < intervals.length; i++ ) {
        if ( intervals[i][0] <= merged[merged.length - 1][1] ) {
            merged[merged.length - 1][1] = Math.max( merged[merged.length - 1][1], intervals[i][1] );
        } else {
            merged.push( Array.from( intervals[i] ) );
        }
    }


    return merged;
};

// [[1,3],[6,9]] ... [4, 5]
// [[1,3],[6,9]] ... [4, 10]
// [[1,3],[6,9]] ... [2, 5]
// [[1,3],[6,9]] ... [2, 6]
// [[1,3],[6,9]] ... [0, 0]
// [[1,3],[6,9]] ... [0, 7]
// [[1,3],[6,9]] ... [10, 11]
