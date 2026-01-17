def _get_starts(graph):
    # 'graph' is the 'self' instance passed from Solution
    return [0]

def _process(node, graph, meta):
    # 1. Pre-Order: Add to current path
    # We skip 0 because it was added during initialization
    if node != 0: 
        graph.current_path.append(node)
    
    # 2. Victory Check
    if node == graph.target:
        graph.results.append(list(graph.current_path))

def _on_exit(node, child_results, graph):
    # 3. Post-Order (Backtracking): Remove from path
    # This replaces your old _post_process hook
    if node != 0:
        graph.current_path.pop()
    return child_results

def _get_neighbors(node, graph):
    for neighbor in graph.adj[node]:
        yield neighbor

def _is_valid(node, graph):
    return True

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # 1. SETUP
        # The 'graph' input is already an adjacency list (index -> neighbors)
        self.adj = graph
        self.target = len(graph) - 1
        self.results = []
        self.current_path = [0] # Start at 0
        
        # 2. RUN ENGINE (Recursive DFS)
        # iterative=False : Use Recursive Engine
        # backtrack=True  : Enable _unmark behavior (though we handle path manually)
        solve(
            graph=self, 
            iterative=False, 
            backtrack=True,
            metadata=False
        )
        return self.results