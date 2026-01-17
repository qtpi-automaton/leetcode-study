def _get_starts(graph):
    # graph is 'self'
    # Start BFS from the Capital (0)
    graph.visited[0] = True
    return [0]

def _get_neighbors(node, graph):
    # Logic: Traverse the tree outwards from 0.
    # Side Effect: Calculate cost while expanding.
    # Iterate through pre-processed adjacency list
    for neighbor, cost in graph.adj[node]:
        
        # MANUAL GUARD CLAUSE (Required because in_place=True)
        if not graph.visited[neighbor]:
            
            # 1. Update Result (Side Effect)
            graph.count += cost
            
            # 2. Mark as Visited
            graph.visited[neighbor] = True
            
            # 3. Handover to Engine
            yield neighbor

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 1. SETUP: Adjacency List
        # We build the graph specifically for this problem.
        # Tuple Format: (neighbor_index, cost_to_traverse)
        self.adj = [[] for _ in range(n)]
        
        for u, v in connections:
            # Original direction u->v. 
            # If we traverse u->v (away from 0), we are going WITH the arrow.
            # But we want arrows pointing TO 0. So this is "Wrong". Cost = 1.
            self.adj[u].append((v, 1))
            
            # Artificial direction v->u.
            # If we traverse v->u (away from 0), we are going AGAINST the arrow.
            # This means the arrow points TO 0. This is "Correct". Cost = 0.
            self.adj[v].append((u, 0))
            
        # 2. State Management
        self.count = 0
        self.visited = [False] * n
        
        # 3. Trigger Engine
        # in_place=True: Tells Engine "Don't track visited nodes, I'll do it."
        solve(graph=self, bfs=True, in_place=True)
        
        return self.count

# --- Boilerplate Hooks ---
# We don't need these validation/processing steps for this specific algorithm
def _is_valid(node, graph): return True
def _process(node, graph, meta): pass

