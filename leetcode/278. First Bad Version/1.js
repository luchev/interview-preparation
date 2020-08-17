/**
 * Complexity (n = number of versions)
 * Time complexity: O(log(n))
 * Space complexity: O(1)
 */
var solution = function ( isBadVersion ) {
    /**
     * isBadVersion(X) returns whether version number X is bad or not
     */
    return function ( n ) {
        let start = 1;
        let end = n;

        let leftMostBadVersion = n + 1;
        while ( end - start >= 0 ) {
            let mid = Math.ceil( ( end + start ) / 2 );
            if ( isBadVersion( mid ) ) {
                leftMostBadVersion = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return leftMostBadVersion;
    };
};
