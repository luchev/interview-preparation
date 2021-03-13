/**
 * Complexity (n = items in arr)
 * Time complexity: O(n^2)
 * Space complexity: O(n)
 */

func numFactoredBinaryTrees(arr []int) int {
	sort.Ints(arr)
	count := make(map[int]int64, len(arr))
	for _, x := range arr {
		count[x] = 1
	}

	for endIndex, a := range arr {
		for _, b := range arr[:endIndex+1] {
			if a%b == 0 {
				reminder := a / b
				if count[reminder] != 0 {
					count[a] += count[b] * count[reminder]
				}
			}
		}
	}

	result := int64(0)
	for _, c := range count {
		result += c
	}
	return int(result % 1000000007)
}
