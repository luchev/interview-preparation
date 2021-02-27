/**
 * Complexity (n = result)
 * Time complexity: O(log(n))
 * Space complexity: O(1)
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
   public:
    int divide(int dividend, int divisor) {
        if (dividend == -2147483648 && divisor == -1) {
            return 2147483647;
        }

        int HALF_INT_MIN = -1073741824;

        int negatives = 2;
        if (dividend > 0) {
            dividend = -dividend;
            negatives -= 1;
        }
        if (divisor > 0) {
            divisor = -divisor;
            negatives -= 1;
        }

        int highest_power = -1;
        int highest_double = divisor;
        while (highest_double >= HALF_INT_MIN && dividend < highest_double + highest_double) {
            highest_power += highest_power;
            highest_double += highest_double;
        }

        int result = 0;
        while (dividend <= divisor) {
            if (dividend <= highest_double) {
                dividend -= highest_double;
                result += highest_power;
                cout << highest_power << "\n";
            }

            highest_power >>= 1;
            highest_double >>= 1;
        }

        if (negatives == 1) {
            return result;
        } else {
            return -result;
        }
    }
};
