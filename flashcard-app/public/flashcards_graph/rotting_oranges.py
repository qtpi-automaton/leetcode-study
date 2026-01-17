def _get_starts(graph):
    # Logic: 
    # 1. Collect all initially rotten oranges ('2') as starts.
    # 2. Count all fresh oranges ('1') to know if we finish successfully later.
    starts = []
    for r in range(graph.rows):
        for c in range(graph.cols):
            val = graph.grid[r][c]
            if val == 2:
                starts.append((r, c))
            elif val == 1:
                graph.fresh_count += 1
    return starts

def _get_neighbors(node, graph):
    # Logic: Infection Spread.
    # We immediately mutate '1' -> '2' here. This effectively 'marks' it.
    r, c = node
    
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        
        # 1. Bounds Check
        if 0 <= nr < graph.rows and 0 <= nc < graph.cols:
            
            # 2. State Check (Is it a Fresh Orange?)
            if graph.grid[nr][nc] == 1:
                # 3. Mutate (Rot it immediately!)
                # This acts as our "visited" check for future nodes.
                graph.grid[nr][nc] = 2
                graph.fresh_count -= 1
                
                yield (nr, nc)

def _process(node, graph, meta):
    # Logic: Track the passage of time.
    # meta: The BFS Level (Minutes elapsed).
    # Simply keep track of the deepest level reached.
    graph.max_minutes = max(graph.max_minutes, meta)

def _is_valid(node, graph):
    # Validation handled in _get_neighbors for In-Place efficiency
    return True

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 1. Setup Context
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        self.fresh_count = 0
        self.max_minutes = 0
        
        # 2. Run Engine
        # is_multi=True : Start BFS from all '2's at once (Level 0).
        # in_place=True : We don't need a 'visited' set; we mutate grid 1 -> 2.
        # metadata=True : We need 'meta' to track the minute (BFS Depth).
        solve(
            graph=self, 
            bfs=True, 
            is_multi=True, 
            in_place=True, 
            metadata=True
        )
        
        # 3. Final Check
        # If fresh_count > 0, it means some oranges were unreachable (isolated).
        return self.max_minutes if self.fresh_count == 0 else -1