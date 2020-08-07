#include <string>
#include <unordered_set>
#include <iostream>
using namespace std;

#define max(a, b) a > b ? a : b

/**
 * Complexity (n = string length)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
int lengthOfLongestSubstring(string s) {
    int maxSubstringSoFar = 0;
    int characters[128];
    for (int i = 0; i < 128; i++) {
        characters[i] = -1;
    }

    int lastRepeatingIndex = 0;
    for (int i = 0; i < s.size(); i++) {
        if (characters[s[i]] != -1) {
            lastRepeatingIndex = max(characters[s[i]] + 1, lastRepeatingIndex);
        }
        
        characters[s[i]] = i;

        maxSubstringSoFar = max(maxSubstringSoFar, i - lastRepeatingIndex + 1);
    }

    return maxSubstringSoFar;
}

int main() {
    std::cout << lengthOfLongestSubstring("abcabcaa");
    return 0;
}