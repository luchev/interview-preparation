/**
 * Complexity (n = board rows, m = board columns, k = word length)
 * Time complexity: O(n * m * 4^3)
 * Space complexity: O(k)
 */
var exist = function ( board, word ) {
    for ( let row = 0; row < board.length; row++ ) {
        for ( let col = 0; col < board[row].length; col++ ) {
            if ( board[row][col] === word[0] ) {
                if ( findPath( board, row, col, word ) ) {
                    return true;
                }
            }
        }
    }

    return false;
};

function findPath( board, row, col, word ) {
    if ( word.length === 0 ) {
        return true;
    }
    if ( board[row] && board[row][col] && board[row][col] !== word[0] ) {
        return false;
    }
    if ( !board[row] || !board[row][col] ) {
        return false;
    }

    word = word.substr( 1 );

    let positionBackup = board[row][col];
    board[row][col] = '_';

    let pathExists = findPath( board, row + 1, col, word ) ||
        findPath( board, row - 1, col, word ) ||
        findPath( board, row, col + 1, word ) ||
        findPath( board, row, col - 1, word );

    board[row][col] = positionBackup;

    return pathExists;
}
