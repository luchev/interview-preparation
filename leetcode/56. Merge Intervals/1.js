/**
 * Complexity (n = array length)
 * Time complexity: O(n * log(n))
 * Space complexity: O(n)
 */
var merge = function ( intervals ) {
    if ( intervals.length === 0 ) {
        return [];
    }
    intervals.sort( ( a, b ) => a[0] - b[0] );

    let mergedIntervals = [intervals[0]];
    for ( let i = 1; i < intervals.length; i++ ) {
        if ( mergedIntervals[mergedIntervals.length - 1][1] >= intervals[i][0] ) {
            mergedIntervals[mergedIntervals.length - 1][1] =
                Math.max( intervals[i][1], mergedIntervals[mergedIntervals.length - 1][1] );
        } else {
            mergedIntervals.push( intervals[i] );
        }
    }

    return mergedIntervals;
};
