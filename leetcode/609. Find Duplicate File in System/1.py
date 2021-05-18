# Complexity (n = number of paths, k = number of files in paths, y = max path+file-name length)
# Time complexity: O(n * k * y)
# Space complexity: O(n * k * y)

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        for x in paths:
            split = x.split(' ')
            directory = split[0]
            files = split[1:]
            for file in files:
                split = file.split('(')
                name = split[0]
                content = split[1]
                mem[content].append(directory + '/' + name)
        return [x for x in mem.values() if len(x) > 1]