# Complexity (n = input list size)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stak = []
        for x in tokens:
            try:
                stak.append(int(x))
            except:
                b = stak.pop()
                a = stak.pop()
                if x == '+':
                    stak.append(a + b)
                elif x == '-':
                    stak.append(a - b)
                elif x == '*':
                    stak.append(a * b)
                elif x == '/':
                    stak.append(int(a / b))
        return stak[-1]