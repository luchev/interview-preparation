# Complexity (n = length of input string)
# Time complexity: O(2^n * n)
# Space complexity: O(2^n * n)

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []
        
        def dfs(stringList, index):
            if index == len(stringList):
                result.append(''.join(stringList))
                return
            
            if stringList[index].isalpha():
                stringList[index] = stringList[index].swapcase()
                dfs(stringList, index + 1)
                stringList[index] = stringList[index].swapcase()
        
            dfs(stringList, index + 1)
            
        
        dfs(list(S), 0)
        return result
