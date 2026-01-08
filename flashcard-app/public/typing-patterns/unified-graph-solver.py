from collections import deque

class UnifiedGraphSolver:
    def solve(self, data, mode="bfs", track_meta=False, use_visited=True, is_multi_source=False):
        visited = ({} if track_meta else set()) if use_visited else None
        result = self._init_result(visited)
        all_starts = self._get_start_points(data)

        if mode == "bfs" and is_multi_source:
            self._bfs(all_starts, data, visited, track_meta)
        else:
            for start in all_starts:
                if not self._check_visited(visited, start):
                    result = self._update_result(result)
                    nodes = [start]
                    if mode == "bfs": self._bfs(nodes, data, visited, track_meta)
                    else:                self._dfs(nodes, data, visited, track_meta)
        return result

