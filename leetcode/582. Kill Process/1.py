# Complexity (n = number of processes (pid-s))
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List
from collections import defaultdict

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = defaultdict(list)
        
        def buildTree():
            for i in range(len(pid)):
                tree[ppid[i]].append(pid[i])
        
        def dfs(root: int, kills: List[int]):
            kills.append(root)
            if root not in tree:
                return
            for x in tree[root]:
                dfs(x, kills)

        buildTree()
        kills = []
        dfs(kill, kills)
        return kills
