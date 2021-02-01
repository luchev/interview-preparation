/**
 * Complexity (n = number of nuts)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

func minDistance(height int, width int, tree []int, squirrel []int, nuts [][]int) int {
	result := 0
	for _, nut := range nuts {
		result += 2 * manhattan(tree, nut)
	}

	best_result := result + manhattan(squirrel, tree)

	for _, nut := range nuts {
		best_result = min(best_result, result+manhattan(squirrel, nut)-manhattan(nut, tree))
	}

	return best_result
}

func manhattan(a []int, b []int) int {
	return abs(a[0]-b[0]) + abs(a[1]-b[1])
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
