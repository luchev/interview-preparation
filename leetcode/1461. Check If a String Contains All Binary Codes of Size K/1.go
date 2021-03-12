/**
 * Complexity (n = string length, k = length of binary codes to look for)
 * Time complexity: O(n) = O(2^k)
 * Space complexity: O(n) = O(2^k)
 */

func hasAllCodes(s string, k int) bool {
	if len(s) < k {
		return false
	}
	set := make([]bool, 1<<k)
	hash := 0
	mask := (1 << k) - 1
	nChars := len(s)
	for index := 0; index < nChars; index += 1 {
		hash = ((hash << 1) & mask)
		if s[index] == '1' {
			hash += 1
		}

		if index >= k-1 {
			set[hash] = true
		}
	}

	for i := 0; i < len(set); i += 1 {
		if set[i] == false {
			return false
		}
	}

	return true
}
