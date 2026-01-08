from collections import deque

class UnifiedGraphSolver:
    def _dfs(self, start_nodes, data, visited, track_meta):
        container = []
        for node in start_nodes:
            container.append((node, None))

        while container:
            curr, parent = container.pop()
            if self._check_visited(visited, curr): continue

            self._mark(visited, curr, parent, track_meta)
            self._process_node(curr, 0)

            for neighbor in self._get_neighbors(curr, data):
                if self._is_valid(neighbor, data) and not self._check_visited(visited, neighbor):
                    container.append((neighbor, curr))
