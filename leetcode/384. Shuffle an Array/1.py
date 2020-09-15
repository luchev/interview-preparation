# Complexity(n = input string length)
# Time complexity: O(n)
# Space complexity: O(ALPHABET_SIZE)


import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffled = self.nums.copy()
        # Simple shuffle algorithm by Fisher and Yates'
        for index in range(0, len(shuffled) - 1):
            swapIndex = random.randint(index, len(shuffled) - 1)
            shuffled[index], shuffled[swapIndex] = shuffled[swapIndex], shuffled[index]

        return shuffled
