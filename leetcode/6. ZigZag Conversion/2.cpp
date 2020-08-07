#include <iostream>
#include <vector>
#include <string>
using namespace std;

/*
PAYPALISHIRING, 3, PAHNAPLSIIGYIR
P   A   H   N
A P L S I I G
Y   I   R
*/

/*
PAYPALISHIRING, 4, PAHNAPLSIIGYIR
P     I    N
A   L S  I G
Y A   H R
P     I
*/

/**
 * Complexity (n = string length)
 * Time complexity: O(n)
 * Space complexity: O(n)
*/
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            return s;
        }

        string result;
        int cycleLength = 2 * numRows - 2;
        int sLen = s.length();

        for (int i = 0; i < numRows; i++) {
            for (int k = 0; k + i < sLen;k += cycleLength) {
                result += s[k + i];
                if (i != 0 && i != numRows - 1 && k + cycleLength - i < sLen) {
                    result += s[k + cycleLength - i];
                }
            }
        }
        return result;
    }
};

int main() {
    Solution solution;
    int rows;
    string in;
    cin >> in;
    cin >> rows;
    cout << solution.convert(in, rows);
}