# Complexity (n = queries)
# Time complexity: O(1) per operation
# Space complexity: O(n)

from typing import List

class FreqStack:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.freqGroups = [[]]

    def push(self, x: int) -> None:
        currentFreq = self.frequency[x] + 1
        self.frequency[x] = currentFreq
        if len(self.freqGroups) == currentFreq:
            self.freqGroups.append([])
        self.freqGroups[currentFreq].append(x)

    def pop(self) -> int:
        result = self.freqGroups[-1].pop()
        self.frequency[result] -= 1
        if len(self.freqGroups[-1]) == 0:
            self.freqGroups.pop()
        return result


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
