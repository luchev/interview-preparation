/**
 * Complexity (n = size of nums)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var twoSum = function(nums, target) {
    let numbers = {};
    for (i = 0; i < nums.length; i++) {
      if (numbers[target - nums[i]] === undefined) {
        numbers[nums[i]] = i;
      } else {
        return [numbers[target - nums[i]], i];
      }
    }
    
    return [-1, -1]
 };
 
