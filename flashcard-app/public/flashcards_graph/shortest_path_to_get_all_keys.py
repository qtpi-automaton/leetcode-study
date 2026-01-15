class Solution(GraphSolver):
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
                    # Bitmask math: set the bit corresponding to the letter
                    self.target_mask |= (1 << (ord(char) - ord('a')))
        
        self.start_node = (start_r, start_c, 0) # (r, c, current_keys)

        # 2. RUN SOLVER
        # BFS (Shortest Path), Metadata (Distance tracking)
        self.solve(grid, bfs=True, metadata=True)
        
        return self.result

    # --- HOOKS ---

    def _get_starts(self, graph):
        return [self.start_node]

    def _process(self, node, meta):
        # Check if we have collected all keys
        r, c, mask = node
        if mask == self.target_mask:
            # If this is the first time we found it, save result
            if self.result == -1: self.result = meta

    def _get_neighbors(self, node, graph):
        # Optimization: If we found the answer, stop generating work
        if self.result != -1: return

        r, c, mask = node
        
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            # We calculate the NEW mask here (State Transition)
            new_mask = mask
            
            # Check if valid first to avoid index errors or logic on invalid cells
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                char = self.grid[nr][nc]
                
                # If it's a key, pick it up (Update Mask)
                if 'a' <= char <= 'f':
                    new_mask |= (1 << (ord(char) - ord('a')))
                
                yield (nr, nc, new_mask)

    def _is_valid(self, neighbor, graph):
        r, c, mask = neighbor
        
        # 1. Check Bounds
        if not (0 <= r < self.rows and 0 <= c < self.cols): return False
        
        char = self.grid[r][c]
        
        # 2. Check Walls
        if char == '#': return False
        
        # 3. Check Locks
        if 'A' <= char <= 'F':
            # Check if we have the bit for this lock
            required_bit = 1 << (ord(char) - ord('A'))
            if not (mask & required_bit):
                return False # Locked!
                
        return True