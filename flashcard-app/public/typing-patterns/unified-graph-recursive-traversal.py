def _traverse_recursive(graph, node, marked, parent, metadata, dp, backtrack):
    if not _is_valid(node, graph, marked): return None
    if _is_marked(node, marked):
        if dp: return marked[node]
        return None

    if not dp:
        _mark(node, marked, parent, metadata)

    _on_enter(node, graph, 0)

    child_results = []
    for neighbor in _get_neighbors(node, graph):
        child_result = _traverse_recursive(graph, neighbor, marked, node, metadata, dp, backtrack)
        if child_result is not None:
            child_results.append(child_result)

    result = _on_exit(node, child_results, graph)

    if dp:
        _mark(node, marked, result, metadata=True)
    elif backtrack:
        _unmark(node, marked)

    return result
