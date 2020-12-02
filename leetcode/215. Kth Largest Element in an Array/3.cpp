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
        std::nth_element(nums.begin(), nums.begin() + k - 1, nums.end(), std::greater<int>());
        return *(nums.begin() + k - 1);
    }
};
