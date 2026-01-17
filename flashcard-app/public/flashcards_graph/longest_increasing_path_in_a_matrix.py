def _init_result(marked):
    # Result accumulator starts at 0
    return 0

def _update_result(result, val):
    # We want the Global Maximum path length found so far
    return max(result, val)

def _get_starts(graph):
    # We must try starting from EVERY cell
    starts = []
    for r in range(graph.rows):
        for c in range(graph.cols):
            starts.append((r, c))
    return starts

def _get_neighbors(node, graph):
    r, c = node
    val = graph.grid[r][c]
    
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        
        # 1. Bounds Check
        if 0 <= nr < graph.rows and 0 <= nc < graph.cols:
            # 2. Increasing Condition (Strictly Greater)
            if graph.grid[nr][nc] > val:
                yield (nr, nc)

def _on_exit(node, child_results, graph):
    """
    The DP Recurrence Relation:
    LIP(node) = 1 + max(LIP(neighbors))
    """
    # If no valid neighbors (child_results is empty), max is 0.
    max_child_path = max(child_results) if child_results else 0
    
    return 1 + max_child_path

# Standard boilerplate
def _is_valid(node, graph): return True
def _process(node, graph, meta): pass


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 1. SETUP
        self.grid = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        
        # 2. RUN ENGINE
        # dp=True: Enables memoization
        # iterative=False: Uses the recursive engine
        return solve(
            graph=self, 
            iterative=False, 
            dp=True
        )
