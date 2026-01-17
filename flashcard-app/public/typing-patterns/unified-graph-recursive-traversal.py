def _traverse_recursive(graph, node, marked, parent, metadata, backtrack):
    if not _is_valid(node, graph) or _is_marked(node, marked):
        return None

    _mark(node, marked, parent, metadata)
    _process(node, graph, 0)

    child_results = []
    for neighbor in _get_neighbors(node, graph):
        child_result = _traverse_recursive(graph, neighbor, marked, node, metadata, backtrack)
        if child_result is not None:
            child_results.append(child_result)

    result = _on_exit(node, child_results, graph)

    if backtrack:
        _unmark(node, marked)

    return result
