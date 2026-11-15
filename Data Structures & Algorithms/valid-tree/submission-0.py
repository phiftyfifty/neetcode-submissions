from collections import defaultdict
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # Build an undirected graph (bidirectional edges)
        for [a, b] in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        # Runtime: O(V + E) traversal
        # Space: O(V + E) recursion calls 
        def check_cycle(node: int, parent: int) -> bool:
            if node in visited:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                # Skip the edge going back to the parent
                if neighbor == parent:
                    continue
                if check_cycle(neighbor, node):
                    return True
            return False
        # Start DFS from node 0 and check for cycles
        if check_cycle(0, -1):
            return False
        # Check if all nodes were visited (meaning the graph is connected)
        return len(visited) == n
            