/**
 * Complexity (n = number items in the array)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
func kLengthApart(nums []int, k int) bool {
	dist := k + 1
	for _, x := range nums {
		if x == 0 {
			dist += 1
		} else if x == 1 && dist >= k {
			dist = 0
		} else {
			return false
		}
	}
	return true
}
