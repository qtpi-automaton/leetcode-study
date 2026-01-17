def solve(graph, in_place=False, metadata=False, iterative=True, is_multi=False, bfs=True, weighted=False, backtrack=False, dp=False):
    marked = _init_marked(in_place, metadata, dp) 
    result = _init_result(marked)
    starts = _get_starts(graph)

    if iterative and is_multi:
        _traverse(graph, starts, marked, metadata, bfs, weighted)
        return result
    for start in starts:
        if _is_marked(start, marked): continue
        if iterative:
            result = _update_result(result)
            _traverse(graph, [start], marked, metadata, bfs, weighted)
        else:
            val = _traverse_recursive(graph, start, marked, None, metadata, backtrack, dp)
            result = _update_result(result, val)
    return result
