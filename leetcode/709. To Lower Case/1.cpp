// Complexity(n = input string length)
// Time complexity : O(n)
// Space complexity : O(1)

#include <string>
using namespace std;

class Solution {
public:
    string toLowerCase(string s) {
        for (auto& x : s) {
            if ('A' <= x && x <= 'Z') {
                x = x + ('a' - 'A');
            }
        }
        return s;
    }
};
