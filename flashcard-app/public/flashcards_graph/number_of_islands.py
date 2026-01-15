class Solution(GraphSolver):
    def _init_result(self, marked):
        # Initialize result as counter (0) instead of using marked object
        return 0
        
    def _get_starts(self, grid):
        # Find all land cells ('1') as potential starting points
        starts = []
        if not grid or not grid[0]:
            return starts
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    starts.append((i, j))
        return starts
    
    def _get_neighbors(self, node, grid):
        # Get valid adjacent land cells (up, down, left, right)
        i, j = node
        neighbors = []
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                neighbors.append((ni, nj))
        return neighbors
    
    def _is_valid(self, node, grid):
        # A cell is valid if it's land ('1')
        i, j = node
        return grid[i][j] == '1'
    
    def _update_result(self, result):
        # Increment island count
        return result + 1
    
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.solve(grid, bfs=True, is_multi=False, in_place=False, metadata=False)
