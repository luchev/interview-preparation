/**
 * Complexity (n = number of words, q = number of queries)
 * Time complexity: O(n + q)
 * Space complexity: O(n + q)
 */

func spellchecker(wordlist []string, queries []string) []string {
	dict := make(map[string]int)

	wordlistset := make(map[string]struct{})
	for _, word := range wordlist {
		wordlistset[word] = struct{}{}
	}

	for index, word := range wordlist {
		lower := strings.ToLower(word)
		_, ok := dict[lower]
		if !ok {
			dict[lower] = index
		}
	}

	for index, word := range wordlist {
		preprocessed := processVowels(word)
		_, ok := dict[preprocessed]
		if !ok {
			dict[preprocessed] = index
		}
	}

	fmt.Println(dict)
	corrected := make([]string, 0)
	for _, s := range queries {
		_, ok := wordlistset[s]
		if ok {
			corrected = append(corrected, s)
			continue
		}

		index, ok := dict[strings.ToLower(s)]
		if ok {
			corrected = append(corrected, wordlist[index])
			continue
		}

		index, ok = dict[processVowels(s)]
		if ok {
			corrected = append(corrected, wordlist[index])
			continue
		}

		corrected = append(corrected, "")
	}

	return corrected
}

func processVowels(s string) string {
	preprocessed := strings.ToLower(s)
	preprocessed = strings.Map(func(r rune) rune {
		switch r {
		case 'a', 'e', 'i', 'o', 'u':
			return '_'
		default:
			return r
		}
	}, preprocessed)
	return preprocessed
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}
