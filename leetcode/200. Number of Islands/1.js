/**
 * Complexity (n = cells in the grid)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var numIslands = function ( grid ) {
    let islands = 0;

    let visited = new Set();

    for ( let row = 0; row < grid.length; row++ ) {
        for ( let col = 0; col < grid[row].length; col++ ) {
            if ( grid[row][col] === '1' && !visited.has( JSON.stringify( [row, col] ) ) ) {
                islands++;
                explore( grid, visited, row, col );
            }
        }
    }

    return islands;
};

function explore( grid, visited, startRow, startCol ) {
    let stack = [[startRow, startCol]];
    while ( stack.length > 0 ) {
        let current = stack.pop();
        for ( let coord of [[-1, 0], [1, 0], [0, -1], [0, 1]] ) {
            let row = coord[0];
            let col = coord[1];
            if ( grid[current[0] + row] && grid[current[0] + row][current[1] + col] === '1' &&
                !visited.has( JSON.stringify( [current[0] + row, current[1] + col] ) ) ) {
                stack.push( [current[0] + row, current[1] + col] );
                visited.add( JSON.stringify( [current[0] + row, current[1] + col] ) );
            }
        }
    }
}
