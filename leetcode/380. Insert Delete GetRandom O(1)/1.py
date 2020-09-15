# Complexity(n = number of queries)
# Space complexity: O(n)
# Insert Time complexity: O(1) Amortized
# Remove Time complexity: O(1) Amortized
# GetRandom Time complexity: O(1) Amortized

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [[] for x in range(0, 11)]
        self.elementCount = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.elementCount >= len(self.table):
            newTable = [[] for x in range(0, (len(self.table) * 2 + 1))]
            for list_ in self.table:
                for element in list_:
                    newTable[element % len(newTable)].append(element)
            self.table = newTable
        
        if val in self.table[val % len(self.table)]:
            return False
        
        self.table[val % len(self.table)].append(val)
        self.elementCount += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        try:
            self.table[val % len(self.table)].remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.elementCount == 0:
            return 0
        while True:
            list_ = self.table[random.randint(0, len(self.table) - 1)]
            if len(list_) >= 1:
                return list_[random.randint(0, len(list_) - 1)]
