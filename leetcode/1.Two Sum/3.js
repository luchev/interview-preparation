/**
 * Complexity (n = largest number in n)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var twoSum = function(nums, target) {
    let maxNum = Math.max(...nums);
    let minNumber = Math.min(...nums);
    let add = 0;
    
    if (minNumber < 0) {
        add = -minNumber;
    }
    maxNum += add;
    
    let numbers = new Array(maxNum + 1);
    let indices = new Array(maxNum + 1);
    let indices2 = new Array(maxNum + 1);
    
    for (i = 0; i < nums.length; i++) {
      
        if (numbers[nums[i] + add] == undefined) {
            numbers[nums[i] + add] = 1;
            indices[nums[i] + add] = i;
        } else {
          numbers[nums[i] + add]++;
          indices2[nums[i] + add] = i;
        }
    }

    target = target + add + add;
    let left = 0;
    let right = maxNum;
    
    while (numbers[left] == undefined) {
        left++;
        
    }
    while (numbers[right] == undefined) {
        right--;
    }

    while (left < right) {
        let sum = left + right;
        if (sum == target)  {
            return [indices[left], indices[right]];
        } else if (sum < target) {
            left++;
            while (numbers[left] == undefined) {
                left++;
            }
        }
        else {
            right--;
            while (numbers[right] == undefined) {
                right--;
            }
        }
    }

    if (left + left == target && indices[left + add] != undefined && indices2[left + add] != undefined) {
      return [indices[left + add], indices2[left + add]];
    }
    
    return [-1, -1];
};

