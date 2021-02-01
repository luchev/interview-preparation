/**
 * Complexity
 * Time complexity: O(1) because the number always has 32 bits
 * Space complexity: O(1)
 */

func hammingWeight(num uint32) int {
	bits := 0
	for i := 0; i < 32; i += 1 {
		bits += int(num & 1)
		num >>= 1
	}
	return bits
}
