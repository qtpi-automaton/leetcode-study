class Solution:
    def solveNQueens(self, n: int):
        # 1. Run the solver. It returns a list of lists: [[1, 3, 0, 2], [2, 0, 3, 1]]
        # We pass 'n' as graph. backtrack=True is needed to clean up 'marked'.
        raw_solutions = solve(graph=n, iterative=False, backtrack=True)
        
        # 2. Format the output (Convert col indices to ".Q.." strings)
        return self._format_output(raw_solutions, n)

    def _format_output(self, solutions, n):
        formatted = []
        for cols in solutions:
            board = []
            for c in cols:
                board.append("." * c + "Q" + "." * (n - c - 1))
            formatted.append(board)
        return formatted

# --- TEMPLATE OVERRIDES ---

def _init_result(marked): 
    return []

def _update_result(result, val):
    # 'val' is the return from one specific start node (one branch of the tree)
    if val is not None:
        result.extend(val)
    return result

def _get_starts(n):
    return [(0, c) for c in range(n)]

def _get_neighbors(node, n):
    r, c = node
    if r == n - 1: return []
    return [(r + 1, col) for col in range(n)]

def _is_valid(node, n, marked):
    # The constraints check (as discussed)
    r, c = node
    if not (0 <= r < n and 0 <= c < n): return False
    for (qr, qc) in marked:
        if c == qc or abs(r - qr) == abs(c - qc):
            return False
    return True

def _on_exit(node, child_results, n):
    r, c = node
    
    # CASE 1: Leaf Node (We are at the bottom row)
    # We found a valid placement! Return it as a single solution path.
    if r == n - 1:
        return [[c]]
    
    # CASE 2: Dead End (No children returned valid paths)
    if not child_results:
        return None
        
    # CASE 3: Internal Node (Bubble Up)
    # child_results is a list of lists of partial paths.
    # Example: child_results = [ [[1, 3, 0]], [[2, 0, 3]] ]
    # We need to flatten and prepend OUR column 'c' to each path.
    my_paths = []
    for child_batch in child_results:
        for path in child_batch:
            my_paths.append([c] + path)
            
    return my_paths