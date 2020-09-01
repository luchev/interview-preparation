#include <string>
#include <unordered_set>
#include <iostream>
using namespace std;

/**
 * Complexity (n = string length)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
int lengthOfLongestSubstring(string s) {
    unordered_set<char> currentLetters;
    size_t maxSubstringSoFar = 0;
    size_t start = 0;
    for (size_t end = 0; end < s.size(); end++) {
        while (currentLetters.count(s[end]) > 0) {
            currentLetters.erase(s[start]);
            start++;
        }
        currentLetters.insert(s[end]);
        if (currentLetters.size() > maxSubstringSoFar) {
            maxSubstringSoFar = currentLetters.size();
        }
    }

    return maxSubstringSoFar;
}

int main() {
    std::cout << lengthOfLongestSubstring("bbbbb");
    return 0;
}