def traverse_recursive(node, parent):
    if not is_valid(node): return None
    if is_marked(node, marked):
        return marked[node] if dp else None

    if not dp:
        mark(node, marked, parent, metadata)

    on_enter(node, parent)

    child_results = []
    for neighbor in get_neighbors(node):
        child_result = traverse_recursive(neighbor, node)
        if child_result is not None:
            child_results.append(child_result)

    res = on_exit(node, child_results)

    if dp: mark(node, marked, res, metadata=True)
    elif backtrack: unmark(node, marked)

    return res
