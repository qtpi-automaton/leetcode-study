
class Solution(GraphSolver):
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        self.fresh_count = 0
        self.max_minutes = 0
        
        # 1. SETUP & RUN
        # We perform a scan inside _get_starts to count fresh oranges too
        self.solve(grid, bfs=True, is_multi=True, in_place=True, metadata=True)
        
        # 2. FINAL CHECK
        return self.max_minutes if self.fresh_count == 0 else -1

    # --- HOOKS ---

    def _get_starts(self, graph):
        starts = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 2:
                    starts.append((r, c))
                elif self.grid[r][c] == 1:
                    self.fresh_count += 1
        return starts

    def _get_neighbors(self, *args):
        r, c = args[0]
        # Standard directions
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            # TRICK: For In-Place BFS, we must mutate BEFORE yielding
            # to prevent the neighbor from being added by someone else.
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] == 1:
                    self.grid[nr][nc] = 2 # Make it rotten immediately
                    self.fresh_count -= 1
                    yield (nr, nc)

    def _is_valid(self, *args):
        # We handled bounds and state checks inside _get_neighbors 
        # to support the in-place mutation trick.
        return True

    def _process(self, *args):
        node, meta = args
        # meta is the Level (Time)
        self.max_minutes = max(self.max_minutes, meta)
