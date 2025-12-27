**Back (The Answer):**
```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)

def dfs(graph, node, visited):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(graph, nei, visited)

# Grid: directions = [(0,1), (0,-1), (1,0), (-1,0)]
def grid_bfs(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    visited = {(r, c)}
    queue = deque([(r, c)])

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
```
