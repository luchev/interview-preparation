/**
 * Complexity (n = number)
 * Time complexity for preprocessing: O(log(n) ^ 2)
 * Space complexity: O(log(n) ^ 2)
 * Time complexity for every call: O(log(n))
 */

var powers map[string]struct{} = make(map[string]struct{})

func reorderedPowerOf2(N int) bool {
	if len(powers) == 0 {
		initPowers()
	}

	_, ok := powers[intToSortedString(N)]
	return ok
}

func intToSortedString(i int) string {
	str := []rune(fmt.Sprintf("%v", i))
	sort.Slice(str, func(i int, k int) bool { return str[i] < str[k] })
	return string(str)
}

// Preprocessing
func initPowers() {
	for i := int(1); i != (1 << 31); i <<= 1 {
		powers[intToSortedString(i)] = struct{}{}
	}
}
