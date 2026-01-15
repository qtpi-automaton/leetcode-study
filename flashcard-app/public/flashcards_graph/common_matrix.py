def _get_starts(self, grid):
        # GENERIC: Scan every cell. If it matches criteria (e.g. "1"), it's a start.
        # Use this for "Number of Islands" or "Connected Components"
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": # <--- CHANGE THIS CONDITION AS NEEDED
                    yield (r, c)

    def _get_neighbors(self, node, grid):
        # GENERIC: The "4-Direction" Cross
        r, c = node
        #                 Right   Left     Down    Up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            yield (r + dr, c + dc)

    def _is_valid(self, node, grid):
        # GENERIC: Bounds Check
        r, c = node
        rows, cols = len(grid), len(grid[0])
        # 1. Inside the box?
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        # 2. Is it a wall/water? (Optional but common)
        if grid[r][c] == "0": # <--- CHANGE THIS CONDITION AS NEEDED
            return False
        return True