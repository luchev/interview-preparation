#include <iostream>
#include <string>
using namespace std;

/**
 * Complexity (n = string length)
 * Time complexity: O(n^3)
 * Space complexity: O(1)
*/
class Solution {
public:
    string longestPalindrome(string s) {
        for (int i = s.length(); i >= 0; i--) {
            for (int k = 0; k <= s.length() - i; k++) {
                if (isPalindrome(s, k, k + i - 1)) {
                    return s.substr(k, i);
                }
            }
        }
        return "";
    }

    bool isPalindrome(const string& s, int start, int end) {
        for (int i = 0; i <= (end - start) / 2; i++) {
            if (s[start + i] != s[end - i]) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution solution;
    string in;
    cin >> in;
    cout << solution.longestPalindrome(in);
}