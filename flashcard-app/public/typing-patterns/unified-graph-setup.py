import heapq
from collections import deque

def solve(graph, in_place=False, metadata=False, iterative=True, is_multi=False, bfs=True, weighted=False, backtrack=False):

def _init_marked(in_place, metadata):
    if in_place: return None
    if metadata: return {}
    return set()

def _init_result(marked): return marked

def _get_starts(graph): return []

def _traverse(graph, starts, marked, metadata, bfs, weighted):
    
def _traverse_recursive(graph, node, marked, parent, metadata, backtrack):

def _is_marked(node, marked):
    if marked is None: return False
    return node in marked

def _update_result(result, val=None): return result

def _mark(node, marked, parent, metadata):
    if marked is None: return
    if metadata: marked[node] = parent
    else: marked.add(node)

def _process(node, graph, meta): pass

def _get_neighbors(node, graph): return []

def _is_valid(node, graph): return True

def _get_weight(node, neighbor): return 1

def _on_exit(node, child_results, graph): return child_results

def _unmark(node, marked):
    if isinstance(marked, set): marked.discard(node)
    elif isinstance(marked, dict): del marked[node]


