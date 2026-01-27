def traverse(nodes):
    if weighted: con = []
    elif bfs:    con = deque()
    else:        con = []

    for node in nodes:
        if weighted:
            heapq.heappush(con, (0, node))
        elif bfs:
            mark(node, marked, None, metadata)
            con.append((0, node))
        else:
            con.append((None, node))

    while con:
        if weighted:      meta, node = heapq.heappop(con)
        elif bfs:         meta, node = con.popleft()
        else:             meta, node = con.pop()

        if not bfs:
            if is_marked(node, marked): continue
            mark(node, marked, meta, metadata)

        on_enter(node, meta)

        for neighbor in get_neighbors(node):
            if is_valid(neighbor):
                if weighted:
                    new_cost = meta + get_weight(node, neighbor)
                    if not is_marked(neighbor, marked):
                        heapq.heappush(con, (new_cost, neighbor))
                elif bfs:
                    if not is_marked(neighbor, marked):
                        mark(neighbor, marked, node, metadata)
                        con.append((meta + 1, neighbor))
                else:
                    if not is_marked(neighbor, marked):
                        con.append((node, neighbor))
