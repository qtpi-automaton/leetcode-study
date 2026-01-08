from collections import deque
from enum import Enum, auto

class Mode(Enum): 
    BFS = auto()
    DFS = auto()

class UnifiedGraphSolverDFS:
    def solve(self, data, track_meta=False, use_visited=True):
        visited = ({} if track_meta else set()) if use_visited else None
        result = self._init_result(visited)
        all_starts = self._get_start_points(data)
        
        for start in all_starts:
            if not self._check_visited(visited, start):
                result = self._update_result(result)
                self._dfs([start], data, visited, track_meta)
        return result

    def _dfs(self, start_nodes, data, visited, track_meta):
        container = []
        for node in start_nodes:
            container.append((node, None))
        
        while container:
            curr, parent = container.pop() 
            if self._check_visited(visited, curr): 
                continue
            self._mark(visited, curr, parent, track_meta)
            self._process_node(curr, 0) 
            
            for neighbor in self._get_neighbors(curr, data):
                if self._is_valid(neighbor, data) and not self._check_visited(visited, neighbor):
                    container.append((neighbor, curr))

    def _check_visited(self, visited, node):
        if visited is None: 
            return False 
        return node in visited

    def _mark(self, visited, node, prev, track_meta):
        if visited is None: 
            return 
        if track_meta: 
            visited[node] = prev
        else:          
            visited.add(node)

    def _init_result(self, visited): 
        return visited
    def _update_result(self, result): 
        return result
    def _is_multi_source(self): 
        return False 
    def _get_start_points(self, data): 
        return []
    def _get_neighbors(self, node, data): 
        return []
    def _is_valid(self, node, data): 
        return True
    def _process_node(self, node, level): 
        pass