/**
 * @param {character[][]} matrix
 * @return {number}
 */
/**
 * Complexity (n = columns, m = rows)
 * Time complexity: O(n * m)
 * Space complexity: O(n * m)
 * Space complexity can be reduced by keeping information only about the last row/column
 */
var maximalSquare = function(matrix) {
    if (matrix === undefined || matrix.length == 0) {
        return 0;
    }
    
    let dp = [];
    let maxSide = 0;
    
    for (let row = 0; row < matrix.length; row++) {
        let value = parseInt(matrix[row][0]);
        dp.push([value]);
        maxSide = Math.max(value, maxSide);
    }
    
    for (let col = 1; col < matrix[0].length; col++) {
        let value = parseInt(matrix[0][col]);
        dp[0].push(value);
        maxSide = Math.max(value, maxSide);
    }
    
    for (let row = 1; row < matrix.length; row++) {
        for (let col = 1; col < matrix[row].length; col++) {
            if (matrix[row][col] === '1') {
                let minAdjacent = Math.min( Math.min( dp[row - 1][col], dp[row][col - 1] ), dp[row - 1][col - 1] )
                dp[row].push(minAdjacent + 1);
                maxSide = Math.max(maxSide, minAdjacent + 1,)
            } else {
                dp[row].push(0);
            }
        }
    }
    
    return maxSide * maxSide;
};
