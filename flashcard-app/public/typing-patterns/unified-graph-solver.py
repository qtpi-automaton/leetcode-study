class GraphSolver:
    def solve(self, graph, bfs=True, is_multi_source=False, in_place=False, track_meta=False):
        marked = self._init_marked(in_place, track_meta)
        result = self._init_result(marked)
        start_nodes = self._get_start_nodes(graph)
        
        if bfs and is_multi_source:
            self._traverse(graph, bfs, start_nodes, marked, track_meta)
        else:
            for start_node in start_nodes:
                if not self._is_marked(start_node, marked):
                    result = self._update_result(result)
                    self._traverse(graph, bfs, [start_node], marked, track_meta)
        return result

