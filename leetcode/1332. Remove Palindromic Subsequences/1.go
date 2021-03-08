/**
 * Complexity (n = length of input string)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

func removePalindromeSub(s string) int {
	if isPalindrome(s) && len(s) > 0 {
		return 1
	} else {
		set := make(map[rune]struct{})
		for _, char := range s {
			set[char] = struct{}{}
		}
		return len(set)
	}
}

func isPalindrome(s string) bool {
	runes := []rune(s)
	for i := 0; i < len(s)/2; i += 1 {
		if runes[i] != runes[len(s)-i-1] {
			return false
		}
	}
	return true
}
