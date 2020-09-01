/**
 * Complexity (n = size of nums)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var twoSum = function(nums, target) {
    let set = new Set();
    for (i = 0; i < nums.length; i++) {
        set.add(nums[i]);
    }
    
    console.log(set);

    return [-1, -1]
 };
 
 