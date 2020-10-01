# Complexity (n = number of queries)
# Time complexity: O(1) per query
# Space complexity: O(n) for all queries

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mins = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.mins) > 0:
            self.mins.append(min(self.mins[-1], x))
        else:
            self.mins.append(x)

    def pop(self) -> None:
        self.data.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]
