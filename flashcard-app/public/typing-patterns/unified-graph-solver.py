from collections import deque
from enum import Enum, auto

class Mode(Enum): 
    BFS = auto()
    DFS = auto()

class UnifiedGraphSolver:
    def _get_start_points(self, *args): return []
    def _get_neighbors(self, *args): return []
    def _is_valid(self, *args): return True
    def _process_node(self, *args): pass
    
    def _init_result(self, *args): return args[0]
    def _update_result(self, *args): return args[0]
    def _is_multi_source(self): return False

    def _check_visited(self, visited, node):
        return visited is not None and node in visited

    def _mark(self, visited, node, prev, track_meta):
        if visited is None: return 
        if track_meta: visited[node] = prev
        else:          visited.add(node)

    def solve(self, data, mode=Mode.BFS, track_meta=False, use_visited=True):
        visited = ({} if track_meta else set()) if use_visited else None
        result = self._init_result(visited)
        all_starts = self._get_start_points(data)
        
        if mode == Mode.BFS and self._is_multi_source():
            self._bfs(all_starts, data, visited, track_meta)
        else:
            for start in all_starts:
                if not self._check_visited(visited, start):
                    result = self._update_result(result)
                    nodes = [start]
                    if mode == Mode.BFS: self._bfs(nodes, data, visited, track_meta)
                    else:                self._dfs(nodes, data, visited, track_meta)
        return result

