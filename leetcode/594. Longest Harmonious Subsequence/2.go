/**
 * Complexity (n = integers in the array)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */

func findLHS(nums []int) int {
	counter := make(map[int]int)
	for _, x := range nums {
		counter[x] += 1
	}
	longest := 0
	for key, count := range counter {
		plusOneCount := counter[key+1]
		if plusOneCount != 0 && longest < count+plusOneCount {
			longest = count + plusOneCount
		}
	}
	return longest
}
