/**
 * Complexity (n = string length)
 * Time complexity: O(n)
 * Space complexity: O(1)
*/
#include <string>
#include <limits.h>
using namespace std;
class Solution {
public:
    int myAtoi(string str) {
        int readingIndex = 0;
        while (str[readingIndex] == ' ') {
            readingIndex++;
        }

        long long number = 0;
        bool isNegative = false;
        if (str[readingIndex] == '-') {
            isNegative = true;
            readingIndex++;
        } else if (str[readingIndex] == '+') {
            readingIndex++;
        }

        while ('0' <= str[readingIndex] && str[readingIndex] <= '9') {
            number *= 10;
            number += str[readingIndex] - '0';
            readingIndex++;
            
            if (isNegative) {
                if (-number < INT_MIN) {
                    return INT_MIN;
                }
            } else if (number > INT_MAX) {
                return INT_MAX;
            }
        }
        
        if (isNegative) {
            return -number;
        } else {
            return number;
        }
    }
};
