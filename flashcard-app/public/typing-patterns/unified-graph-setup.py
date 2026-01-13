from collections import deque

class GraphSolver:
    def solve(self, graph, bfs=True, is_multi=False, in_place=False, metadata=False):

    def _init_marked(self, in_place, metadata):
        if in_place: return None
        if metadata: return {}
        else: return set()
    def _init_result(self, marked):
        return marked
    def _get_starts(self, graph):
        return []

    def _traverse(self, graph, bfs, starts, marked, metadata):

    def _is_marked(self, node, marked):
        if marked is None: return False
        else: return node in marked

    def _update_result(self, result):
        return result

    def _mark(self, node, marked, parent, metadata):
        if marked is None: return
        if metadata: marked[node] = parent
        else: marked.add(node)
    def _process(self, node, meta):
        pass
    def _get_neighbors(self, node, graph):
        return []
    def _is_valid(self, node, graph):
        return True
