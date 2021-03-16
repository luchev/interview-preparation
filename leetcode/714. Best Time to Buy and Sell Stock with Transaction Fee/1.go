/**
 * Complexity (n = number of prices)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

func maxProfit(prices []int, fee int) int {
	cash := 0
	hold := -prices[0]
	for i := 1; i < len(prices); i += 1 {
		cash = max(cash, hold+prices[i]-fee)
		hold = max(hold, cash-prices[i])
	}
	return cash
}

func max(a int, b int) int {
	if a < b {
		return b
	}
	return a
}
