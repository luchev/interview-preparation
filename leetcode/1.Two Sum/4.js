/**
 * This solution is an improvement over the sorting method and the 
 * counting method, by choosing the better one to use
 * In case of sparse input (few numbers but big in size) - sorting
 * In case of big input (many numbers) - counting
 */
var twoSum = function(nums, target) {
    if (nums.length < 20) {
        return twoSumBruteForce(nums, target);
    }

    let maxNum = Math.max(...nums);
    let minNumber = Math.min(...nums);
    let shift = 0;
    
    if (minNumber < 0) {
        shift = -minNumber;
    }

    maxNum += shift;

    let log = Math.log(maxNum) / Math.log(2);
    if (3 * log < nums.length) {
        return twoSumSort(nums, target);
    } else {
        return twoSumSort(nums, target, maxNum, shift);
    }
};

var twoSumBruteForce = function(nums, target) {
    for (i = 0; i < nums.length; i++) {
        for (j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j];
            }
        }
    }
     return [-1, -1]
 };

var twoSumSort = function(nums, target) {
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

var twoSumCounting = function(nums, target, maxNum, shift) {
    
    let numbers = new Array(maxNum + 1);
    let indices = new Array(maxNum + 1);
    let indices2 = new Array(maxNum + 1);
    
    for (i = 0; i < nums.length; i++) {
      
        if (numbers[nums[i] + shift] == undefined) {
            numbers[nums[i] + shift] = 1;
            indices[nums[i] + shift] = i;
        } else {
          numbers[nums[i] + shift]++;
          indices2[nums[i] + shift] = i;
        }
    }

    target = target + shift + shift;
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

    if (left + left == target && indices[left + shift] != undefined && indices2[left + shift] != undefined) {
      return [indices[left + shift], indices2[left + shift]];
    }
    
    return [-1, -1];
};
