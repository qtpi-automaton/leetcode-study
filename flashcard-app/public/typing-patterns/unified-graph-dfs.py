def _traverse(self, graph, bfs, starts, marked, metadata):
    con = []
    for node in starts:
        con.append((node, None))
    while con:
        node, meta = con.pop()
        if self._is_marked(node, marked): continue
        self._mark(node, marked, meta, metadata)
        self._process(node, 0)
        for neighbor in self._get_neighbors(node, graph):
            if self._is_valid(neighbor, graph) and not self._is_marked(neighbor, marked):
                con.append((neighbor, node))

