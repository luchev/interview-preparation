/**
 * Complexity (n = size of nums)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var twoSum = function(nums, target) {
    let numbers = {};
    let searchForNumber = 0;
    for (i = 0; i < nums.length; i++) {
      searchForNumber = numbers[target - nums[i]];
      if (searchForNumber === undefined) {
        numbers[nums[i]] = i;
      } else {
        return [searchForNumber, i];
      }
    }
    
    return [-1, -1]
 };
 
