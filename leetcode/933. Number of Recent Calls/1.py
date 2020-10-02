# Complexity (n = number of queries)
# Time complexity: O(1) amortized per query
# Space complexity: O(n) or O(interval_length) if a queue is used instead of array

class RecentCounter:
    def __init__(self):
        self.pings = []
        self.left = 0

    def ping(self, t: int) -> int:
        self.pings.append(t)
        lower_bound = t - 3000
        while self.pings[self.left] < lower_bound:
            self.left += 1
        return len(self.pings) - self.left
