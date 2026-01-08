from collections import deque

class GraphSolver:
    def _bfs(self, graph, start_nodes, visited, track_meta):
        container = deque()
        for node in start_nodes:
            self._mark(visited, node, None, track_meta)
            container.append((node, 0))
        while container:
            current_node, level = container.popleft()
            self._process_node(current_node, level)
            for neighbor_node in self._get_neighbors(current_node, graph):
                if self._is_valid(neighbor_node, graph) and not self._check_visited(visited, neighbor_node):
                    self._mark(visited, neighbor_node, current_node, track_meta)
                    container.append((neighbor_node, level + 1))
