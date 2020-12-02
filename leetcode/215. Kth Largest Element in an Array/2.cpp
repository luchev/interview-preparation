/**
 * Complexity (n = input array size, k = number of closest points to pick)
 * Time complexity: O(k * log(n))
 * Space complexity: O(n)
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
   public:
    int findKthLargest(vector<int>& nums, int k) {
        std::make_heap(nums.begin(), nums.end());
        for (int i = 1; i < k; i++) {
            std::pop_heap(nums.begin(), nums.end());
            nums.pop_back();
        }

        return nums[0];
    }
};
