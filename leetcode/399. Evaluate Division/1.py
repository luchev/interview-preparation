# Complexity (n = number of equations, k = number of queries)
# Time complexity: O(n * k)
# Space complexity: O(n)

from typing import List
from collections import defaultdict
import queue

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = build_graph(equations, values)
        return [traverse(graph, start, end) for start, end in queries]

def build_graph(equations: List[List[str]], values: List[float]) -> defaultdict:
    graph = defaultdict(defaultdict)
    for eq, val in zip(equations, values):
        nom, denom = eq
        graph[nom][denom] = val
        graph[denom][nom] = 1 / val
    return graph

def traverse(graph: defaultdict, start: str, end: str) -> float:
    if start not in graph or end not in graph:
        return -1

    visited = set([start])
    que = queue.Queue()
    que.put((start, 1))
    while que.qsize() > 0:
        current, accumulated = que.get()
        if current == end:
            return accumulated
        for neighbour, value in graph[current].items():
            if neighbour not in visited:
                que.put((neighbour, accumulated * value))
                visited.add(neighbour)

    return -1
