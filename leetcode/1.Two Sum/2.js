/**
 * Complexity (n = size of nums)
 * Time complexity: O(n * lgn)
 * Space complexity: O(n)
 */
var twoSum = function(nums, target) {
    let numsPairs = [];
    for (i = 0; i < nums.length; i++) {
        numsPairs.push({index: i, num: nums[i]})
    }
    numsPairs.sort(function(a, b) {return a.num - b.num; });

    let left = 0;
    let right = nums.length - 1;
    console.log(numsPairs)
    while (left != right) {
        let sum = numsPairs[left].num + numsPairs[right].num;
        if (sum == target) {
            return [numsPairs[left].index, numsPairs[right].index];
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return [-1, -1];
};
