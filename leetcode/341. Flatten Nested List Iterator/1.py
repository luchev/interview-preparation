# Complexity (n = size of input list, k = max depth of nested lists)
# Time complexity: O(1) per operation
# Space complexity: O(k) as a whole


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.peeked = None
        self.data = nestedList
        self.generator = self.dfs_gen(nestedList)
    
    def next(self) -> int:
        if not self.hasNext():
            return None
        next_val = self.peeked
        self.peeked = None
        return next_val
    
    def hasNext(self) -> bool:
        if self.peeked is not None:
            return True
        try:
            self.peeked = next(self.generator)
            return True
        except:
            return False

    def dfs_gen(self, nestedList: List[NestedInteger]):
        for item in nestedList:
            if item.isInteger():
                yield item.getInteger()
            else:
                yield from self.dfs_gen(item.getList())
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())