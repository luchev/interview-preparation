/**
 * Complexity (s = number of words, t = average word length)
 * Time complexity: O(s * t)
 * Space complexity: O(t) not counting the result
 */

/**
 * @param {string[]} words
 * @param {string} pattern
 * @return {string[]}
 */
 var findAndReplacePattern = function(words, pattern) {
    let result = [];
    for (let word of words) {
        if (isIsomorphic(word, pattern)) {
            result.push(word);
        }
    }
    return result;
};

function isIsomorphic(s, t) {
    if (s.length !== t.length) {
        return false;
    }
    let sToT = {}; // todo better names for this hash map
    let tToS = {};
    
    for (let i = 0; i < s.length; i++) {
        if (sToT[s[i]] === undefined) {
            sToT[s[i]] = t[i];
        } else {
            if (sToT[s[i]] !== t[i]) {
                return false;
            }
        }
        
        if (tToS[t[i]] === undefined) {
            tToS[t[i]] = s[i];
        } else {
            if (tToS[t[i]] !== s[i]) {
                return false;
            }
        }
    }
    
    return true;
};
