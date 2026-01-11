class GraphSolver:
    def _traverse(self, graph, bfs, start_nodes, marked, track_meta):
        if bfs: container = deque()
        else: container = []

        for node in start_nodes:
            if bfs:
                self._mark(node, marked, None, track_meta)
                container.append((node, 0))
            else: container.append((node, None))

        while container:
            if bfs: node, meta = container.popleft()
            else: node, meta = container.pop()

            if bfs: self._process(node, meta)
            else:
                if self._is_marked(node, marked): continue
                self._mark(node, marked, meta, track_meta)
                self._process(node, 0)

            for neighbor in self._get_neighbors(node, graph):
                if self._is_valid(neighbor, graph) and not self._is_marked(neighbor, marked):
                    if bfs:
                        self._mark(neighbor, marked, node, track_meta)
                        container.append((neighbor, meta + 1))
                    else: container.append((neighbor, node))

