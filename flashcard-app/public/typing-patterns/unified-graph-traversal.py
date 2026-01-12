class GraphSolver:
    def _traverse(self, graph, bfs, starts, marked, metadata):
        if bfs: con = deque()
        else: con = []

        for node in starts:
            if bfs:
                self._mark(node, marked, None, metadata)
                con.append((node, 0))
            else: con.append((node, None))

        while con:
            if bfs: node, meta = con.popleft()
            else: node, meta = con.pop()

            if bfs: self._process(node, meta)
            else:
                if self._is_marked(node, marked): continue
                self._mark(node, marked, meta, metadata)
                self._process(node, 0)

            for neighbor in self._get_neighbors(node, graph):
                if self._is_valid(neighbor, graph) and not self._is_marked(neighbor, marked):
                    if bfs:
                        self._mark(neighbor, marked, node, metadata)
                        con.append((neighbor, meta + 1))
                    else: con.append((neighbor, node))

