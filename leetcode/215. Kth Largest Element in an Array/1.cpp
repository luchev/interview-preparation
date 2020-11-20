/**
 * Complexity (n = input array size)
 * Time complexity: O(n) expected
 * Time complexity: O(n^2) worst case
 * Space complexity: O(1)
 */

#include <vector>
using namespace std;
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int left = 0;
        int right = nums.size() - 1;
        int pivot = partition(nums, left, right);
        while (pivot != nums.size() - k) {
            if (pivot > nums.size() - k) {
                right = pivot - 1;
            } else {
                left = pivot + 1;
            }
            pivot = partition(nums, left, right);
        }
        return nums[pivot];
    }
    
    int partition(vector<int>& nums, int left, int right) {
        int slow = left;
        int pivot = right;
        
        for (int fast = left; fast < right; fast++) {
            if (nums[fast] < nums[pivot]) {
                swap(nums[fast], nums[slow]);
                slow++;
            }
        }
        
        swap(nums[pivot], nums[slow]);
        return slow;
    }
};
