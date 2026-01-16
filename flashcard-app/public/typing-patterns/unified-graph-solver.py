def solve(graph, bfs=True, iterative=True, weighted=False, backtrack=False, in_place=False, metadata=False):
    marked = _init_marked(in_place, metadata)
    result = _init_result(marked)
    starts = _get_starts(graph)

    if iterative:
        _traverse(graph, bfs, weighted, starts, marked, metadata)
    else:
        for start in starts:
            if not _is_marked(start, marked):
                result = _update_result(result)
                _traverse_recursive(graph, start, marked, None, metadata, backtrack)
    return result