
from collections import defaultdict

class Solution(GraphSolver):
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.email_to_name = {}
        self.graph = defaultdict(set)
        
        # 1. BUILD GRAPH
        # Edge: Connect first email to all other emails in the list
        for account in accounts:
            name = account[0]
            first_email = account[1]
            
            # Map every email to the name (we just need it once per group)
            for email in account[1:]:
                self.email_to_name[email] = name
                self.graph[first_email].add(email)
                self.graph[email].add(first_email)
        
        # 2. RUN SOLVER
        # Use DFS to find connected components
        self.groups = defaultdict(list)
        self.current_group_id = -1
        
        # We don't need the return value of solve, we use self.groups
        self.solve(self.graph, bfs=False, in_place=False)
        
        # 3. FORMAT OUTPUT
        result = []
        for group_id, emails in self.groups.items():
            emails.sort()
            name = self.email_to_name[emails[0]]
            result.append([name] + emails)
            
        return result

    # --- HOOKS ---

    def _get_starts(self, graph):
        # We need to iterate over every email to find all components
        return list(self.graph.keys())

    def _get_neighbors(self, node, graph):
        # node is an email (string)
        for neighbor in self.graph[node]:
            yield neighbor

    def _update_result(self, result):
        # This hook runs once BEFORE starting a new component.
        # We use it to increment our ID counter.
        self.current_group_id += 1
        return result

    def _process(self, *args):
        node, meta = args
        # Add the current email to the current group list
        self.groups[self.current_group_id].append(node)