from collections import deque

class UnifiedGraphSolver:
    def _bfs(self, start_nodes, data, visited, track_meta):
        container = deque()
        for node in start_nodes:
            self._mark(visited, node, None, track_meta)
            container.append((node, 0))

        while container:
            curr, level = container.popleft() 
            self._process_node(curr, level)
            
            for neighbor in self._get_neighbors(curr, data):
                if self._is_valid(neighbor, data) and not self._check_visited(visited, neighbor):
                    self._mark(visited, neighbor, curr, track_meta)
                    container.append((neighbor, level + 1)) 

