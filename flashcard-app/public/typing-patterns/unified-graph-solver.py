from collections import deque

class UnifiedGraphSolver:
    def solve(self, data, mode=Mode.BFS, track_meta=False, use_visited=True):
        visited = ({} if track_meta else set()) if use_visited else None
        result = self._init_result(visited)
        all_starts = self._get_start_points(data)
        
        if mode == Mode.BFS and self._is_multi_source():
            self._bfs(all_starts, data, visited, track_meta)
        else:
            for start in all_starts:
                if not self._check_visited(visited, start):
                    result = self._update_result(result)
                    nodes = [start]
                    if mode == Mode.BFS: self._bfs(nodes, data, visited, track_meta)
                    else:                self._dfs(nodes, data, visited, track_meta)
        return result

