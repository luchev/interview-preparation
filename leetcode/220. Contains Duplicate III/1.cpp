/**
 * Complexity (n = input array size, k = window size)
 * Time complexity: O(n * log(k) )
 * Space complexity: O(k)
 */

#include <set>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        multiset<long long> window;
        for (int i = 0; i < nums.size(); i++) {
            if (i > k) {
                window.erase(nums[i - k - 1]);
            }
            
            auto lower = window.lower_bound((long long)nums[i] - t);
            if (lower != window.end() && abs(*lower - nums[i]) <= t) {
                return true;
            }
            
            window.insert(nums[i]);
        }
        return false;
    }
};
