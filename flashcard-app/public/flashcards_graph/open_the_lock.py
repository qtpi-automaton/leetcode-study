class Solution(GraphSolver):
    def openLock(self, deadends: List[str], target: str) -> int:
        self.dead = set(deadends)
        self.target = target
        self.min_turns = -1
        
        # GOTCHA: If start is dead, we can't even move.
        if "0000" in self.dead: return -1
        
        self.solve(None, bfs=True, metadata=True)
        return self.min_turns

    # --- HOOKS ---

    def _get_starts(self, graph):
        return ["0000"]

    def _process(self, node, meta):
        # meta is the Level (Distance/Turns)
        if node == self.target:
            # BFS guarantees the first time we see it, it's the shortest
            if self.min_turns == -1: 
                self.min_turns = meta

    def _get_neighbors(self, node, graph):
        # Optimization: If we found the answer, stop generating work
        if self.min_turns != -1: return

        for i in range(4):
            digit = int(node[i])
            for move in [-1, 1]:
                # The "Wrap Around" Math: (9 + 1) % 10 -> 0, (0 - 1) % 10 -> 9
                new_digit = (digit + move) % 10
                
                # String slicing to replace just that character
                new_node = node[:i] + str(new_digit) + node[i+1:]
                yield new_node

    def _is_valid(self, neighbor, graph):
        return neighbor not in self.dead
