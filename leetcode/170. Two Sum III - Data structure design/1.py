
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}

    # Complexity (n = number of calls to add())
    # Time complexity: O(1) amortized 
    # Space complexity: O(n) total
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.nums:
            self.nums[number] = 0
        self.nums[number] += 1

    # Complexity (n = number of items in self.nums)
    # Time complexity: O(n)
    # Space complexity: O(1)
    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        half = value >> 1
        if half << 1 == value:
            if half in self.nums and self.nums[half] > 1:
                return True
        for num in self.nums.keys():
            if num != half and value - num in self.nums:
                return True
        return False
