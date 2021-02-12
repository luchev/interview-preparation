/**
 * Complexity (n = initial number)
 * Time complexity: O(log(n))
 * Space complexity: O(log(n))
 */

func numberOfSteps(num int) int {
	steps := 0
	for num > 0 {
		steps += 1
		if num&0b1 == 1 {
			num -= 1
		} else {
			num >>= 1
		}
	}
	return steps
}
