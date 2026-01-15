class Solution(GraphSolver):
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.grid = heights
        self.rows = len(heights)
        self.cols = len(heights[0])
        
        # 1. RUN FOR PACIFIC
        self.current_ocean = "PACIFIC"
        # We need the visited set returned, so in_place=False
        p_visited = self.solve(heights, bfs=True, is_multi=True)
        
        # 2. RUN FOR ATLANTIC
        self.current_ocean = "ATLANTIC"
        a_visited = self.solve(heights, bfs=True, is_multi=True)
        
        # 3. INTERSECTION
        # Python sets allow '&' for intersection
        return list(p_visited & a_visited)

    # --- HOOKS ---

    def _get_starts(self, graph):
        starts = []
        if self.current_ocean == "PACIFIC":
            # Top row and Left col
            for r in range(self.rows): starts.append((r, 0))
            for c in range(self.cols): starts.append((0, c))
        else:
            # Bottom row and Right col
            for r in range(self.rows): starts.append((r, self.cols - 1))
            for c in range(self.cols): starts.append((self.rows - 1, c))
        return starts

    def _get_neighbors(self, node, graph):
        r, c = node
        for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
            # TRICK: We put the logic here because we need 'node' AND 'neighbor'
            # to compare heights. _is_valid only gets 'neighbor'.
            
            # 1. Check Bounds (Standard)
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                # 2. Check Height (Must go UPHILL or equal)
                if self.grid[nr][nc] >= self.grid[r][c]:
                    yield (nr, nc)

    def _is_valid(self, neighbor, graph):
        # We did all checks in _get_neighbors to access the current node height
        return True