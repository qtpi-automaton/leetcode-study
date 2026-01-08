from collections import deque

class GraphSolver:
    def _dfs(self, graph, start_nodes, visited, track_meta):
        container = []
        for node in start_nodes:
            container.append((node, None))
        while container:
            current_node, parent_node = container.pop()
            if self._check_visited(visited, current_node): continue
            self._mark(visited, current_node, parent_node, track_meta)
            self._process_node(current_node, 0)
            for neighbor_node in self._get_neighbors(current_node, graph):
                if self._is_valid(neighbor_node, graph) and not self._check_visited(visited, neighbor_node):
                    container.append((neighbor_node, current_node))

