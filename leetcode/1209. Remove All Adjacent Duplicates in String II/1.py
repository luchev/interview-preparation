# Complexity (n = length of input string)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['', math.inf]]
        
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            
            if stack[-1][1] >= k:
                stack[-1][1] -= k
            if stack[-1][1] == 0:
                stack.pop()
        
        stack[0][1] = 0
        return ''.join(list(x[0] * x[1] for x in stack))