# Complexity (n = length of stamp, k = length of target)
# Time complexity: O(k * (k - n))
# Space complexity: O(k * (k - n)) # including the result

from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        questions = '?' * len(target)
        result = []
        changeOccurred = True
        while changeOccurred and len(result) < 10 * len(target) and target != questions:
            left = 0
            changeOccurred = False
            for left in range(len(target) - len(stamp) + 1):
                if strcmp(stamp, target[left:left + len(stamp)]):
                    result.append(left)
                    target = target[:left] + '?' * len(stamp) + target[left + len(stamp):]
                    changeOccurred = True
        
        if target == questions:
            return result[::-1]
        return []
        
def strcmp(a,b):
    if all(x == '?' for x in b):
        return False
    for i in range(len(a)):
        if a[i] != b[i] and b[i] != '?':
            return False
    return True
