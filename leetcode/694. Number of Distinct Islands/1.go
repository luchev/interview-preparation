/**
 * Complexity (n = grid rows, m = grid cols)
 * Time complexity: O(n * m)
 * Space complexity: O(n * m)
 */

func numDistinctIslands(grid [][]int) int {
	islands := make(map[string]struct{})

	for row := range grid {
		for col := range grid[row] {
			var path bytes.Buffer
			dfs(grid, row, col, &path, "^")
			if path.Len() > 0 {
				islands[path.String()] = struct{}{}
			}
		}
	}

	return len(islands)
}

func dfs(grid [][]int, row int, col int, path *bytes.Buffer, direction string) {
	if row < 0 || len(grid) <= row || col < 0 || len(grid[row]) <= col {
		return
	}
	if grid[row][col] == 0 {
		return
	}
	grid[row][col] = 0
	path.WriteString(direction)
	dfs(grid, row+1, col, path, "D")
	dfs(grid, row-1, col, path, "U")
	dfs(grid, row, col+1, path, "R")
	dfs(grid, row, col-1, path, "L")
	path.WriteString("^")
}
