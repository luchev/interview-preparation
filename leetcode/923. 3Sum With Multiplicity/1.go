/**
 * Complexity (n = length of arr)
 * Time complexity: O(n^2)
 * Space complexity: O(n)
 */

func threeSumMulti(arr []int, target int) int {
	count := make(map[int]int)
	for _, x := range arr {
		count[x] += 1
	}

	unique := make([]int, 0)
	for key, _ := range count {
		unique = append(unique, key)
	}

	sort.Ints(unique)
	tuplesCount := 0
	mod := 1000000007
	for startIndex, a := range unique {
		left := startIndex
		right := len(unique) - 1
		for left <= right {
			sum := a + unique[left] + unique[right]
			if sum == target {
				if a == unique[left] && a == unique[right] {
					tuplesCount += count[a] * (count[a] - 1) * (count[unique[left]] - 2) / 6
				} else if a == unique[left] {
					tuplesCount += count[a] * (count[a] - 1) * count[unique[right]] / 2
				} else if unique[left] == unique[right] {
					tuplesCount += count[a] * count[unique[left]] * (count[unique[left]] - 1) / 2
				} else {
					tuplesCount += count[a] * count[unique[left]] * count[unique[right]]
				}

				if tuplesCount > mod {
					tuplesCount %= mod
				}
			}

			if sum < target {
				left += 1
			} else {
				right -= 1
			}
		}
	}

	return tuplesCount
}
