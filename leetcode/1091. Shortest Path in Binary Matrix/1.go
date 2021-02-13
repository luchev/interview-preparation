/**
 * Complexity (n = rows, m = cols)
 * Time complexity: O(n * m)
 * Space complexity: O(n * m)
 */

type Cell struct {
	row  int
	col  int
	dist int
}

func shortestPathBinaryMatrix(grid [][]int) int {
	que := make([]Cell, 0)
	que = append(que, Cell{0, 0, 1})

	for len(que) > 0 {
		front := que[0]
		que = que[1:]
		row := front.row
		col := front.col
		dist := front.dist

		if row == len(grid)-1 && col == len(grid[row])-1 && grid[row][col] == 0 {
			return dist
		}

		if grid[row][col] == 1 {
			continue
		}
		grid[row][col] = 1

		for drow := -1; drow <= +1; drow += 1 {
			for dcol := -1; dcol <= +1; dcol += 1 {
				nextRow := row + drow
				nextCol := col + dcol
				if 0 <= nextRow && nextRow < len(grid) && 0 <= nextCol && nextCol < len(grid[row]) {
					que = append(que, Cell{nextRow, nextCol, dist + 1})
				}
			}
		}
	}

	return -1
}
