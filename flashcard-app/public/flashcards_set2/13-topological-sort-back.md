**Back (The Answer):**
```python
from collections import deque, defaultdict

def topo_sort(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n

    for src, dst in edges:
        graph[src].append(dst)
        indegree[dst] += 1

    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return result if len(result) == n else []
```
