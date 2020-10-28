/**
 * Complexity (n = input number)
 * Time complexity: O(log(n))
 * Space complexity: O(1)
 */

class Solution {
   public:
    int mySqrt(int x) {
        double upper = x;
        double lower = 0;
        double mid = (upper + lower) / 2;
        // while (abs(mid * mid - x) > 0.00001) {
        for (int i = 0; i < 100; i++) {
            if (mid * mid > x) {
                upper = mid;
            } else if (mid * mid < x) {
                lower = mid;
            }
            mid = (upper + lower) / 2;
        }

        return mid;
    }
};
