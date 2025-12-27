**Back (The Answer):**
```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Grid traversal (4 directions)
def grid_bfs(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    visited = {(start_r, start_c)}
    queue = deque([(start_r, start_c)])
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
```
