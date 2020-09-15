/**
 * Complexity (n = matrix height/width)
 * Time complexity: O(n^2)
 * Space complexity: O(n^2)
 */
var rotate = function ( matrix ) {
    for ( let row of matrix ) {
        row.reverse();
    }

    let mSize = matrix.length;

    for ( let row = 0; row < mSize; row++ ) {
        for ( let col = 0; col < mSize - row - 1; col++ ) {
            [matrix[row][col], matrix[mSize - col - 1][mSize - row - 1]] = [matrix[mSize - col - 1][mSize - row - 1], matrix[row][col]];
        }
    }

    return;
};
