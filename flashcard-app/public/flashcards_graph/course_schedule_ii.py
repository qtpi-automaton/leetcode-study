
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. SETUP STATE (Context)
        self.adj = [[] for _ in range(numCourses)]
        self.indegree = [0] * numCourses
        self.topo_order = []
        
        # Build Graph: [src, dest] means dest depends on src (src -> dest)
        for dest, src in prerequisites:
            self.adj[src].append(dest)
            self.indegree[dest] += 1
            
        # 2. RUN ENGINE
        # We pass 'self' as the graph argument. 
        # The engine will thread 'self' into every hook as 'graph'.
        solve(graph=self, bfs=True)
        
        # 3. CYCLE CHECK
        if len(self.topo_order) == numCourses:
            return self.topo_order
        return []

# --- HOOKS (Functional Logic) ---

def _get_starts(graph):
    # 'graph' is the 'self' instance from Solution
    starts = []
    for i, count in enumerate(graph.indegree):
        if count == 0:
            starts.append(i)
    return starts

def _process(node, graph, meta):
    # Just record the node in our order list
    graph.topo_order.append(node)

def _get_neighbors(node, graph):
    # Logic: Kahn's Algorithm
    # Simulate removing 'node' from the graph by decrementing 
    # the indegree of its neighbors.
    for neighbor in graph.adj[node]:
        graph.indegree[neighbor] -= 1
        
        # CRITICAL: Only yield neighbor if it is now unlocked (0 dependencies)
        if graph.indegree[neighbor] == 0:
            yield neighbor

def _is_valid(node, graph):
    return True