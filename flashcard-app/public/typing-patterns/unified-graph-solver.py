def solve(graph, in_place=False, metadata=False, dp=False,
          iterative=True, is_multi=False, bfs=True, weighted=False,
          backtrack=False, kahn=False, *args):

    marked = init_marked(in_place, metadata, dp)
    result = marked
    indegree = get_indegree(graph) if kahn else None

    def get_starts():
        if indegree is not None:
            starts = []
            for node, count in indegree.items():
                if count == 0:
                    starts.append(node)
            return starts
        if isinstance(graph, list):
            return range(len(graph))
        else:
            return graph.keys()

    def update_result(res, val=None):
        return res

    def on_enter(node, meta):
        pass

    def get_neighbors(node):
        return graph[node]

    def is_valid(node):
        if indegree is not None:
            indegree[node] -= 1
            return indegree[node] == 0
        return True

    def get_weight(node, neighbor):
        return 1

    def on_exit(node, child_results):
        return child_results

    starts = get_starts()
    if iterative and is_multi:
        traverse(starts)
        return result

    for start in starts:
        if is_marked(start, marked): continue

        if iterative:
            result = update_result(result)
            traverse([start])
        else:
            val = traverse_recursive(start, None)
            result = update_result(result, val)

    return result


    # --- 1. CONFIGURATION PRESETS ---
    # PRESETS = {
    #     'kahn':      {'bfs': True, 'is_multi': True, 'indegree': True},
    #     'dijkstra':  {'weighted': True},
    #     'dfs':       {'bfs': False},
    #     'bfs':       {'bfs': True},
    #     'dp':        {'iterative': False, 'dp': True},
    #     'backtrack': {'iterative': False, 'backtrack': True}
    # }