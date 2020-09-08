/**
 * Complexity (n = cells in the grid)
 * Time complexity: O(n)
 * Space complexity: O(n) because we use the input grid to write to it (can be replaced with Visited Nodes Set)
 */
var numIslands = function ( grid ) {
    let islands = 0;

    for ( let row = 0; row < grid.length; row++ ) {
        for ( let col = 0; col < grid[row].length; col++ ) {
            if ( grid[row][col] === '1' ) {
                islands++;
                explore( grid, row, col );
            }
        }
    }

    return islands;
};

function explore( grid, startRow, startCol ) {
    let stack = [[startRow, startCol]];
    while ( stack.length > 0 ) {
        let current = stack.pop();
        for ( let coord of [[-1, 0], [1, 0], [0, -1], [0, 1]] ) {
            let row = current[0] + coord[0];
            let col = current[1] + coord[1];
            if ( grid[row] && grid[row][col] === '1' ) {
                stack.push( [row, col] );
                grid[row][col] = 'x';
            }
        }
    }
}
