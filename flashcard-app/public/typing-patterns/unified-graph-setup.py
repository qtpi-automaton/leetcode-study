def init_marked(in_place, metadata, dp=False):
    if in_place: return None
    if metadata or dp: return {}
    return set()

def get_indegree(graph):
    if isinstance(graph, list): nodes = range(len(graph))
    else: nodes = graph.keys()
    degree = {u: 0 for u in nodes}
    for u in nodes:
        for v in graph[u]:
            degree[v] = degree.get(v, 0) + 1
    return degree

def is_marked(node, marked):
    if marked is None: return False
    return node in marked

def mark(node, marked, meta):
    if marked is None: return
    if isinstance(marked, dict):
        marked[node] = meta        
    else:
        marked.add(node)

def unmark(node, marked):
    if marked is None: return
    if isinstance(marked, dict): del marked[node]
    elif isinstance(marked, set): marked.discard(node)


# import heapq
# from collections import deque
# from collections import defaultdict