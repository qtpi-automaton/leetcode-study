def _get_starts(graph):
    # Return the start node found in pre-scan
    return [graph.start_node]

def _process(node, graph, meta):
    # Logic: Victory Check.
    # If our current mask matches the target mask, we have all keys.
    r, c, mask = node
    if mask == graph.target_mask:
        # Since BFS guarantees shortest path, the first time we see this, it's optimal.
        if graph.result == -1:
            graph.result = meta

def _get_neighbors(node, graph):
    # Logic: Movement & State Transition.
    # Here we determine the 'Next State' (New Mask).
    # Optimization: Stop expanding if we already found the answer
    if graph.result != -1: return

    r, c, mask = node
    
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        
        # 1. Bounds Check (Crucial before accessing grid)
        if 0 <= nr < graph.rows and 0 <= nc < graph.cols:
            char = graph.grid[nr][nc]
            
            # 2. State Transition: Key Pickup
            # If we step on a key, we MUST pick it up (update mask).
            new_mask = mask
            if 'a' <= char <= 'f':
                new_mask |= (1 << (ord(char) - ord('a')))
            
            # Yield the COMPOSITE state
            yield (nr, nc, new_mask)

def _is_valid(node, graph):
    # Logic: The Filter (Walls & Locks).
    r, c, mask = node
    char = graph.grid[r][c]
    
    # 1. Check Walls
    if char == '#': return False
    
    # 2. Check Locks
    if 'A' <= char <= 'F':
        # To pass Lock 'A', we need bit 0. Lock 'B' needs bit 1...
        required_bit = 1 << (ord(char) - ord('A'))
        
        # If we DON'T have the bit in our mask, it's invalid
        if not (mask & required_bit):
            return False
            
    return True

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.target_mask = 0
        self.result = -1
        
        # 1. PRE-SCAN: Find Start (@) and Target Keys (a-f)
        start_r, start_c = 0, 0
        for r in range(self.rows):
            for c in range(self.cols):
                char = grid[r][c]
                if char == '@':
                    start_r, start_c = r, c
                elif 'a' <= char <= 'f':
                    # Bit manipulation: 'a'->0, 'b'->1...
                    self.target_mask |= (1 << (ord(char) - ord('a')))
        
        # Define Start Node: (row, col, current_keys_mask)
        self.start_node = (start_r, start_c, 0)
        
        # 2. RUN SOLVER
        # bfs=True: Shortest Path
        # metadata=True: We need 'meta' to track distance/moves
        solve(graph=self, bfs=True, metadata=True)
        
        return self.result