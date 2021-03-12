/**
 * Complexity (n = length of input string)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

func isStrobogrammatic(num string) bool {
	strobos := map[byte]byte{
		'8': '8',
		'6': '9',
		'9': '6',
		'1': '1',
		'0': '0',
	}
	mid := int(math.Ceil(float64(len(num)) / 2.0))
	for i := 0; i < mid; i += 1 {
		if strobos[num[i]] != num[len(num)-1-i] {
			return false
		}
	}
	return true
}
