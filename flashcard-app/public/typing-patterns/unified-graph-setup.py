from collections import deque

class GraphSolver:
    def solve(self, graph, bfs=True, is_multi_source=False, in_place=False, track_meta=False):

    def _init_visited(self, in_place, track_meta):
        if in_place: return None
        if track_meta: return {}
        else: return set()
    def _init_result(self, visited):
        return visited
    def _get_start_nodes(self, graph):
        return []

    def _traverse(self, graph, bfs, start_nodes, visited, track_meta):

    def _check_visited(self, node, visited):
        if visited is None: return False
        else: return node in visited

    def _update_result(self, result):
        return result

    def _get_neighbors(self, *args):
        return []
    def _is_valid(self, *args):
        return True
    def _process(self, *args):
        pass
    def _mark(self, node, visited, parent, track_meta):
        if visited is None: return
        if track_meta: visited[node] = parent
        else: visited.add(node)