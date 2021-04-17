/**
 * Complexity (n = length of input array)
 * Time complexity: O(n^2)
 * Space complexity: O(n)
 */

func subarraySum(nums []int, k int) int {
	csum := make([]int, len(nums)+1)
	for i := 1; i <= len(nums); i += 1 {
		csum[i] = csum[i-1] + nums[i-1]
	}

	count := 0
	for start := 0; start < len(nums); start += 1 {
		for end := start + 1; end < len(nums)+1; end += 1 {
			if csum[end]-csum[start] == k {
				count += 1
			}
		}
	}
	return count
}
