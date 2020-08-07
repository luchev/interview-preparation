/**
 * Complexity (n = number)
 * Time complexity: O(logn)
 * Space complexity: O(logn)
 */
var isPalindrome = function(x) {
    if (x < 0) {
        return false;
    }
    
    let str = x.toString();
    let len = Math.floor(str.length / 2);
    for (i = 0; i < len ; i++) {
        if (str[i] != str[str.length - i - 1]) {
            return false;
        }
    }
    return true;
};