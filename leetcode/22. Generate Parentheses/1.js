/**
 * Complexity (n = number of pairs of parentheses)
 * Time complexity: O(4^n / n*sqrt(n))
 * Space complexity: O(4^n / n*sqrt(n))
 * For explanation of the complexity visit https://leetcode.com/problems/generate-parentheses/solution/
 * This complexity comes from the Catalan numbers
 */
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function ( n ) {
    combinations = [];
    recursiveGeneration( '', n * 2, 0 );
    return combinations;
};

// Global variable to store all parentheses combinations
var combinations = [];

function recursiveGeneration( str, maxLength, balance ) {
    if ( str.length >= maxLength ) {
        if ( balance === 0 ) {
            combinations.push( str );
        }
        return;
    }

    if ( balance < 0 ) {
        return;
    }

    recursiveGeneration( str + '(', maxLength, balance + 1 );
    recursiveGeneration( str + ')', maxLength, balance - 1 );
}
