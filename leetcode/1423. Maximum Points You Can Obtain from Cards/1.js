/**
 * Complexity (n = number of cards)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var maxScore = function ( cardPoints, k ) {
    let sum = 0;
    for ( let i = 0; i < k; i++ ) {
        sum += cardPoints[i];
    }

    let bestSum = sum;
    for ( let left = k - 1; left >= 0; left-- ) {
        sum -= cardPoints[left];
        sum += cardPoints[cardPoints.length - k + left];
        if ( sum > bestSum ) {
            bestSum = sum;
        }
    }

    return bestSum;
};
