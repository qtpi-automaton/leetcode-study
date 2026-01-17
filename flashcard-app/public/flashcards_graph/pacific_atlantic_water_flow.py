def _get_starts(graph):
    # Logic: Selects edges based on the current ocean context.
    # graph: The Solution instance.
    starts = []
    rows, cols = graph.rows, graph.cols
    
    if graph.current_ocean == "PACIFIC":
        # Left Edge
        for r in range(rows): starts.append((r, 0))
        # Top Edge
        for c in range(cols): starts.append((0, c))
    else: # ATLANTIC
        # Right Edge
        for r in range(rows): starts.append((r, cols - 1))
        # Bottom Edge
        for c in range(cols): starts.append((rows - 1, c))
        
    return starts

def _get_neighbors(node, graph):
    # Logic: Upstream Flow.
    # Water flows High->Low, so we search Low->High.
    r, c = node
    # Reuse simple directions
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        # 1. Bounds Check
        if 0 <= nr < graph.rows and 0 <= nc < graph.cols:
            # 2. Height Check (The "Uphill" Logic)
            # Neighbor must be EQUAL or HIGHER to flow down to us.
            if graph.grid[nr][nc] >= graph.grid[r][c]:
                yield (nr, nc)

def _is_valid(node, graph):
    # Logic handled in _get_neighbors for efficiency
    return True

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []

        # 1. Setup Context
        self.grid = heights
        self.rows = len(heights)
        self.cols = len(heights[0])
        
        # 2. Run Engine for PACIFIC
        self.current_ocean = "PACIFIC"
        # bfs=True, is_multi=True (Start with ALL edges in queue)
        # in_place=False (We need the set returned, don't modify a global)
        pacific_reachable = solve(self, bfs=True, is_multi=True, in_place=False)
        
        # 3. Run Engine for ATLANTIC
        self.current_ocean = "ATLANTIC"
        atlantic_reachable = solve(self, bfs=True, is_multi=True, in_place=False)
        
        # 4. Intersection (Python Set Logic)
        return list(pacific_reachable & atlantic_reachable)