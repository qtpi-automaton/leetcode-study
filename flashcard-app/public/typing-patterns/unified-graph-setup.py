from enum import Enum, auto

class Mode(Enum): 
    BFS = auto()
    DFS = auto()

class UnifiedGraphSolver:
    def _get_start_points(self, *args): return []
    def _get_neighbors(self, *args): return []
    def _is_valid(self, *args): return True
    def _process_node(self, *args): pass
    
    def _init_result(self, visited): return visited
    def _update_result(self, result): return result
    def _is_multi_source(self): return False

    def _check_visited(self, visited, node):
        return visited is not None and node in visited

    def _mark(self, visited, node, prev, track_meta):
        if visited is None: return 
        if track_meta: visited[node] = prev
        else:          visited.add(node)
