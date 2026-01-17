
def solve(graph, in_place=False, metadata=False, iterative=True, is_multi=False, bfs=True, weighted=False, backtrack=False):
    marked = _init_marked(in_place, metadata)
    result = _init_result(marked)
    starts = _get_starts(graph)

    if iterative:
        if is_multi:
            _traverse(graph, starts, marked, metadata, bfs, weighted)
        else:
            for start in starts:
                if not _is_marked(start, marked):
                    result = _update_result(result)
                    _traverse(graph, [start], marked, metadata, bfs, weighted)
    else:
        for start in starts:
            if not _is_marked(start, marked):
                result = _update_result(result)
                _traverse_recursive(graph, start, marked, None, metadata, backtrack)

    return result