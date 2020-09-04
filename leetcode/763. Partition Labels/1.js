/**
 * Complexity (n = input string length)
 * Time complexity: O(n)
 * Space complexity: O(ALPHABET_SIZE)
 */
var partitionLabels = function ( S ) {
    let intervals = {};
    for ( let i = 0; i < S.length; i++ ) {
        let char = S[i];

        if ( intervals[char] === undefined ) {
            intervals[char] = [i, i];
        }

        intervals[char][1] = i;
    }

    let mergedIntervals = [];
    for ( let interval of Object.values( intervals ) ) {
        if ( mergedIntervals.length === 0 ) {
            mergedIntervals.push( interval )
        } else {
            let lastInterval = mergedIntervals.pop();
            if ( lastInterval[1] < interval[0] ) {
                mergedIntervals.push( lastInterval );
                mergedIntervals.push( interval );
            } else {
                lastInterval[1] = Math.max( lastInterval[1], interval[1] );
                mergedIntervals.push( lastInterval );
            }
        }
    }

    return mergedIntervals.map( interval => interval[1] - interval[0] + 1 );
};
