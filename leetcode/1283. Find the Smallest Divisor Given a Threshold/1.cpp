/**
 * Complexity (n = input array size)
 * Time complexity: O(n*log(n))
 * Space complexity: O(1)
 */

#include <cmath>
#include <vector>
using namespace std;
class Solution {
   public:
    int smallestDivisor(vector<int>& nums, int threshold) {
        int left = 1;
        int right = 1000000;
        int best = right;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (check(nums, mid) <= threshold) {
                best = min(best, mid);
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return best;
    }

    int check(vector<int>& nums, double div) {
        int res = 0;
        for (auto x : nums) {
            res += ceil(x / div);
        }
        return res;
    }
};
