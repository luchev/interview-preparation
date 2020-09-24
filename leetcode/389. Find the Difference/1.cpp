/**
 * Complexity (n = length of string s, k = length of string t)
 * Time complexity: O(n + k)
 * Space complexity: O(1)
 */

#include <string>
using namespace std;

class Solution {
   public:
    char findTheDifference(string s, string t) {
        char difference = 0;
        for (char c : s) {
            difference ^= c;
        }
        for (char c : t) {
            difference ^= c;
        }
        return difference;
    }
};
