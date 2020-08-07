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

        vector<string> rows(numRows);
        int row = 0;
        bool goingDown = true;
        for (int i = 0; i < s.length(); i++) {
            rows[row] += s[i];

            if (row == 0) {
                goingDown = true;
            } else if (row == numRows - 1) {
                goingDown = false;
            }

            if (goingDown) {
                row++;
            } else {
                row--;
            }
        }

        string result;
        for (int i = 0; i < rows.size(); i++) {
            result += rows[i];
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