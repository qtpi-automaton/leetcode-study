from collections import deque

class GraphSolver:
    def solve(self, graph, mode="BFS", is_multi_source=False, in_place=False, track_meta=False):
        visited = self._init_visited(track_meta, in_place)
        result = self._init_result(visited)
        start_nodes = self._get_start_nodes(graph)
        
        if mode == "BFS" and is_multi_source:
            self._bfs(graph, start_nodes, visited, track_meta)
        else:
            for start_node in start_nodes:
                if not self._check_visited(visited, start_node):
                    result = self._update_result(result)
                    if mode == "BFS": self._bfs(graph, [start_node], visited, track_meta)
                    else:             self._dfs(graph, [start_node], visited, track_meta)
        return result

