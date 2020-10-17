# Complexity (n = number of logs)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            identifier, data = log.split(' ', 1)

            if data[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((identifier, data))

        letter_logs.sort(key=lambda x: (x[1], x[0]))
        letter_logs = [' '.join(log) for log in letter_logs]
        return letter_logs + digit_logs
