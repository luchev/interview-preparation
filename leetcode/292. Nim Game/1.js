/**
 * Complexity (n = number)
 * Time complexity: O(1)
 * Space complexity: O(1)
 * The pattern can be clearly described with a formula, hence the time/space complexity
*/
var canWinNim = function(n) {
    return n % 4 != 0;
};

// The pattern is
// 1 2 3 <- win
// 4 <- lose
// 5 - 1 -> win
// 6 - 2 -> win
// 7 - 3 -> win
// 8 -> lose
// 9 -> win
// 10 -> win
// 11 -> win
// 12 -> lose
