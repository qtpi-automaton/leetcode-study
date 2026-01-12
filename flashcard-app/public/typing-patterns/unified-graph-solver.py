class GraphSolver:
    def solve(self, graph, bfs=True, is_multi=False, in_place=False, metadata=False):
        marked = self._init_marked(in_place, metadata)
        result = self._init_result(marked)
        starts = self._get_starts(graph)
        
        if bfs and is_multi:
            self._traverse(graph, bfs, starts, marked, metadata)
        else:
            for start in starts:
                if not self._is_marked(start, marked):
                    result = self._update_result(result)
                    self._traverse(graph, bfs, [start], marked, metadata)
        return result

