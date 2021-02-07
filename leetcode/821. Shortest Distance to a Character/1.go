/**
 * Complexity (n = length of input string)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */

func shortestToChar(s string, c byte) []int {
	distance := make([]int, len(s))
	charDist := math.MaxInt32

	for i := 0; i < len(s); i += 1 {
		if s[i] == c {
			charDist = 0
		}
		distance[i] = charDist
		charDist += 1
	}

	charDist = math.MaxInt32
	for i := len(s) - 1; i >= 0; i -= 1 {
		if s[i] == c {
			charDist = 0
		}
		distance[i] = min(distance[i], charDist)
		charDist += 1
	}

	return distance
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}
