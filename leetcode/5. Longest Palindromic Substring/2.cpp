#include <iostream>
#include <string>

#define min(a, b) ((a) < (b) ? (a) : (b))

using namespace std;

/**
 * Complexity (n = string length)
 * Time complexity: O(n^2)
 * Space complexity: O(1)
*/
class Solution {
public:
    string longestPalindrome(string s) {
        int longestPalindromeStart = 0;
        int longestPalindromeLength = 0;
        
        for (int i = 0; i < s.length(); i++) {
            for (int k = 0; k <= min(i, s.length() - i - 1); k++) {
                cout << "i = " << i << " k = " << k << endl;
                if (s[i - k] == s[i + k]) {
                    if (longestPalindromeLength < 1 + 2 * k) {
                        longestPalindromeStart = i - k;
                        longestPalindromeLength = 1 + 2 * k;
                        if (longestPalindromeStart == 0 && longestPalindromeLength == s.length()) {
                            break;
                        }
                    }
                } else {
                    break;
                }
            }
        }

        if (s.length() == 0) {
            return "";
        }
        for (int i = 0; i < s.length() - 1; i++) {
            for (int k = 0; i - k >= 0 && i + k + 1 < s.length(); k++) {
                if (s[i - k] == s[i + k + 1]) {
                    if (longestPalindromeLength < 2 * k + 2) {
                        longestPalindromeStart = i - k;
                        longestPalindromeLength = 2 * k + 2;
                        if (longestPalindromeStart == 0 && longestPalindromeLength == s.length()) {
                            break;
                        }
                    }
                } else {
                    break;
                }
            }
        }

        return s.substr(longestPalindromeStart, longestPalindromeLength);
    }
};

int main() {
    Solution solution;
    string in;
    cin >> in;
    cout << solution.longestPalindrome(in);
}