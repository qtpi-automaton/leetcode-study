class Solution(GraphSolver):
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 1. SETUP: Adjacency List
        # Format: (neighbor, sign)
        # sign=1: Original direction (u->v). Needs flip if we traverse it.
        # sign=0: Artificial direction (v->u). Good direction.
        self.adj = [[] for _ in range(n)]
        for u, v in connections:
            self.adj[u].append((v, 1))
            self.adj[v].append((u, 0))
            
        self.count = 0
        self.visited = [False] * n
        
        # 2. RUN SOLVER
        # We use in_place=True to disable the engine's visited set
        # so we can manage self.visited manually.
        self.solve(n, bfs=True, in_place=True)
        
        return self.count

    # --- HOOKS ---

    def _get_starts(self, graph):
        # Start at City 0
        self.visited[0] = True
        return [0]

    def _get_neighbors(self, node, graph):
        # node is the current city index
        for neighbor, sign in self.adj[node]:
            
            # JAVA LOGIC REPLICATION:
            # Check visited -> Count -> Mark -> Add to Queue
            if not self.visited[neighbor]:
                self.count += sign        # Add cost
                self.visited[neighbor] = True # Mark immediately
                yield neighbor            # Add to Queue

    # Standard boilerplate for hooks we don't use
    def _is_valid(self, *args): return True
    def _process(self, *args): pass