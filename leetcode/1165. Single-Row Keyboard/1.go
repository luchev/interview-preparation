/**
 * Complexity (n = length of word, k = length of keyboard)
 * Time complexity: O(n + k)
 * Space complexity: O(k)
 */

func calculateTime(keyboard string, word string) int {
	if len(word) == 0 {
		return 0
	}

	total := 0
	keys := make(map[rune]int)
	for index, ch := range keyboard {
		keys[ch] = index
	}

	currentKey := rune(keyboard[0])
	for _, ch := range word {
		total += abs(keys[ch] - keys[currentKey])
		currentKey = ch
	}

	return total
}

func abs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}
