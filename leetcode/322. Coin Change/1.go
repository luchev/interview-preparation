/**
 * Complexity (n = amount, k = number of coins)
 * Time complexity: O(n * k)
 * Space complexity: O(n)
 */

func coinChange(coins []int, amount int) int {
	amounts := make([]int, amount+1)

	for am := 1; am < amount+1; am += 1 {
		minCoins := math.MaxInt32
		for _, coin := range coins {
			if coin <= am && amounts[am-coin] < math.MaxInt32 {
				minCoins = min(minCoins, amounts[am-coin]+1)
			}
		}
		amounts[am] = minCoins
	}

	if amounts[len(amounts)-1] == math.MaxInt32 {
		return -1
	}
	return amounts[len(amounts)-1]
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}
