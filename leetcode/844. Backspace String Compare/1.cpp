/**
 * Complexity (s = S length, t = T length)
 * Time complexity: O(s + t)
 * Space complexity: O(s + t)
 */

#include <string>
using namespace std;
class Solution {
   public:
    bool backspaceCompare(string S, string T) {
        return parse(S) == parse(T);
    }

    string parse(string input) {
        string output;
        for (auto c : input) {
            if (c == '#') {
                if (output.size() > 0) {
                    output.pop_back();
                }
            } else {
                output.push_back(c);
            }
        }
        return output;
    }
};
