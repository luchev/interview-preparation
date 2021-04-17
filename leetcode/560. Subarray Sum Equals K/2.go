/**
 * Complexity (n = length of input array)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */

func subarraySum(nums []int, k int) int {
	result := 0
	mp := make(map[int]int)
	mp[0] = 1
	sum := 0
	for _, v := range nums {
		sum += v
		if count, ok := mp[sum-k]; ok {
			result += count
		}
		mp[sum] += 1
	}
	return result
}
