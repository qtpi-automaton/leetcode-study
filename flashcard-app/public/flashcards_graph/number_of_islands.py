
def _init_result(marked): 
    # Initialize result as counter (0)
    return 0

def _update_result(result): 
    # Increment island count when a new start is found
    return result + 1

def _get_starts(grid):
    # Return all '1's as potential starting points
    if not grid or not grid[0]: return []
    starts = []
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                starts.append((r, c))
    return starts

def _get_neighbors(node, grid):
    # Get adjacent coordinates within bounds
    r, c = node
    neighbors = []
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors

def _is_valid(node, grid):
    # Valid only if land ('1')
    r, c = node
    return grid[r][c] == '1'

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Use the generic solve function with specific flags
        return solve(
            graph=grid, 
            bfs=True, 
            is_multi=False, 
            in_place=False, 
            metadata=False
        )
