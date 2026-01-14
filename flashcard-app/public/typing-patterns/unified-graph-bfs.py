def _traverse(self, graph, bfs, starts, marked, metadata):
    con = deque()
    for node in starts:
        self._mark(node, marked, None, metadata)
        con.append((node, 0))
    while con:
        node, meta = con.popleft()
        self._process(node, meta)
        for neighbor in self._get_neighbors(node, graph):
            if self._is_valid(neighbor, graph) and not self._is_marked(neighbor, marked):
                self._mark(neighbor, marked, node, metadata)
                con.append((neighbor, meta + 1))

