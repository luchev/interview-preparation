from queue import Queue

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        transitions = {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
        
        start = "0000"
        frontier = Queue()
        frontier.put([start, 0])
        ends = set(deadends)
        visited = set()
        
        while frontier.qsize() > 0:
            node, dist = frontier.get()
            if node == target:
                return dist
            if node in visited or node in ends:
                continue
            visited.add(node)
            
            nextDist = dist + 1
            for index, char in enumerate(node):
                for tran in transitions[char]:
                    frontier.put([node[:index] + tran + node[index + 1:], nextDist])
            
        return -1