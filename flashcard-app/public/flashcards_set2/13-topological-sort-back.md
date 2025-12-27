**Back (The Answer):**
```python
from collections import deque, defaultdict

def topological_sort(num_nodes, edges):
    # Build graph and indegree count
    graph = defaultdict(list)
    indegree = [0] * num_nodes
    
    for src, dst in edges:
        graph[src].append(dst)
        indegree[dst] += 1
    
    # Start with nodes having no dependencies
    queue = deque([i for i in range(num_nodes) if indegree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # If result has all nodes, valid ordering exists
    return result if len(result) == num_nodes else []
```
