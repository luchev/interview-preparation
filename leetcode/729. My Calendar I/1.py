# Complexity (n = number of queries)
# Time complexity: O(n^2) for all queries
# Space complexity: O(n)

class MyCalendar:

    def __init__(self):
        self.data = []
        
    def book(self, start: int, end: int) -> bool:
        for s, e in self.data:
            if s < end and start < e:
                return False
        self.data.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)