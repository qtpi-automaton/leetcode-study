class GraphSolver:
    def solve(self, graph, bfs=True, is_multi_source=False, in_place=False, track_meta=False):
        visited = self._init_visited(in_place, track_meta)
        result = self._init_result(visited)
        start_nodes = self._get_start_nodes(graph)
        
        if bfs and is_multi_source:
            self._traverse(graph, bfs, start_nodes, visited, track_meta)
        else:
            for start_node in start_nodes:
                if not self._check_visited(start_node, visited):
                    result = self._update_result(result)
                    self._traverse(graph, bfs, [start_node], visited, track_meta)
        return result

