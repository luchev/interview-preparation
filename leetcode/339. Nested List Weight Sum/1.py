# Complexity (n = nexted elements)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class NestedInteger:
   def __init__(self, value=None):
       pass

   def isInteger(self):
       pass

   def add(self, elem):
       pass

   def setInteger(self, value):
       pass

   def getInteger(self):
       pass

   def getList(self):
       pass

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return recursiveDfs(nestedList, 1)
        
def recursiveDfs(nestedList: List[NestedInteger], depth: int) -> int:
    result = 0
    for x in nestedList:
        if x.isInteger():
            result += x.getInteger() * depth
        else:
            result += recursiveDfs(x.getList(), depth + 1)
    return result
