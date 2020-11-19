# Complexity (n = string length, k = max number in front of brackets e.g 42[])
# Time complexity: O(n * k)
# Space complexity: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [[1,[]]]
        num = 0
        for x in s:
            print('Parse', x)
            if x.isnumeric():
                num = num * 10 + int(x)
            elif x == '[':
                stack.append([num,[]])
                num = 0
            elif x == ']':
                top = stack.pop()
                stack[-1][1] = stack[-1][1] + top[0] * top[1]
            else:
                stack[-1][1].append(x)
        return ''.join(stack.pop()[1])
