/**
 * Complexity (n = size of nums)
 * Time complexity: O(n^2)
 * Space complexity: O(1)
 */
var twoSum = function(nums, target) {
   for (i = 0; i < nums.length; i++) {
       for (j = i + 1; j < nums.length; j++) {
           if (nums[i] + nums[j] == target) {
               return [i, j];
           }
       }
   }
    return [-1, -1]
};

