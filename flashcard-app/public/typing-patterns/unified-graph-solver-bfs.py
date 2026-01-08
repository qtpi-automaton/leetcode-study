from collections import deque
from enum import Enum, auto

class Mode(Enum): 
    BFS = auto()
    DFS = auto()

class UnifiedGraphSolver:
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