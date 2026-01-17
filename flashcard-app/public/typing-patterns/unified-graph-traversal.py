def _traverse(graph, starts, marked, metadata, bfs, weighted):
    if weighted: con = []
    elif bfs:    con = deque()
    else:        con = []

    for node in starts:
        if weighted:
            heapq.heappush(con, (0, node))
        elif bfs:
            _mark(node, marked, 0, metadata)
            con.append((0, node))
        else:
            con.append((None, node))

    while con:
        if weighted:
            meta, node = heapq.heappop(con)
        elif bfs:
            meta, node = con.popleft()
        else:
            meta, node = con.pop()

        if not bfs:
            if _is_marked(node, marked): continue
            _mark(node, marked, meta, metadata)

        _process(node, graph, meta)

        for neighbor in _get_neighbors(node, graph):
            if _is_valid(neighbor, graph):
                if weighted:
                    weight = _get_weight(node, neighbor)
                    new_cost = meta + weight
                    if not _is_marked(neighbor, marked):
                        heapq.heappush(con, (new_cost, neighbor))
                elif bfs:
                    if not _is_marked(neighbor, marked):
                        _mark(neighbor, marked, node, metadata)
                        con.append((meta + 1, neighbor))
                else:
                    if not _is_marked(neighbor, marked):
                        con.append((node, neighbor))
