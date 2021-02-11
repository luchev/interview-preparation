/**
 * Complexity (n = max(length string1, length string2))
 * Time complexity: O(n)
 * Space complexity: O(n) Really this is O(ALPHABET_SIZE) but worst case is O(n)
 */

func isAnagram(s string, t string) bool {
	counter := make(map[rune]int)
	for _, char := range s {
		counter[char] += 1
	}

	for _, char := range t {
		counter[char] -= 1
		if counter[char] == 0 {
			delete(counter, char)
		}
	}

	return len(counter) == 0
}
