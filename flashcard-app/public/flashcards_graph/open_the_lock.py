def _get_starts(graph):
    # graph is 'self'
    return ["0000"]

def _process(node, graph, meta):
    """
    Now we have all 3 ingredients:
    1. node (Where we are)
    2. graph/self (The Target State)
    3. meta (The Distance/Turns)
    """
    if node == graph.target:
        # BFS guarantees shortest path, so capture the first time we see it.
        if graph.min_turns == -1:
            graph.min_turns = meta

def _get_neighbors(node, graph):
    # Optimization: Early Exit if answer found
    if graph.min_turns != -1: 
        return

    for i in range(4):
        digit = int(node[i])
        for move in [-1, 1]:
            # Wrap around math
            new_digit = (digit + move) % 10
            # Construct new string
            yield node[:i] + str(new_digit) + node[i+1:]

def _is_valid(node, graph):
    # Check against the dead set stored in self
    return node not in graph.dead

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 1. Setup State (The Context)
        self.dead = set(deadends)
        self.target = target
        self.min_turns = -1
        
        # 2. Guard Clause
        if "0000" in self.dead: return -1
        
        # 3. Trigger Engine
        # We pass 'self' as the graph. Now 'self' flows into every hook.
        solve(
            graph=self, 
            bfs=True, 
            metadata=True # We need metadata to track the depth (turns)
        )
        
        return self.min_turns



