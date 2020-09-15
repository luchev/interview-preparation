/**
 * Complexity (n = number of time points)
 * Time complexity: O(n)
 * Space complexity: O(n) - can be reduced if we parse the strings when we need them
 */
var findMinDifference = function ( timePoints ) {
    let timePointsInts = timePoints.map( x => timeToMinutes( x ) );
    timePointsInts.sort( ( a, b ) => a - b );
    let firstTimestamp = timePointsInts[0] + 24 * 60;
    timePointsInts.push( firstTimestamp );

    let minDifference = timePointsInts[1] - timePointsInts[0];
    for ( let i = 1; i < timePointsInts.length - 1; i++ ) { // 2 < 2
        if ( timePointsInts[i + 1] - timePointsInts[i] < minDifference ) {
            minDifference = timePointsInts[i + 1] - timePointsInts[i];
        }
    }

    return minDifference;
};

function timeToMinutes( timestamp ) {
    let split = timestamp.split( ':' );
    let hours = parseInt( split[0] );
    let minutes = parseInt( split[1] );

    return hours * 60 + minutes;
}
