def solve(data, n, metadata=False):
    parent, rank, meta = _init_ds(n, metadata, data)
    count = _init_count(n)

    for u, v in _get_edges(data):
        if _union(u, v, parent, rank, meta):
            count = _update_count(count)

    return _calc_result(count, meta, metadata)

def _init_ds(n, metadata, data):
    parent = list(range(n))
    rank = [0] * n
    meta = None
    if metadata: meta = _init_meta(n, data)
    return parent, rank, meta

def _init_meta(n, data):
    return [1] * n

def _init_count(n): return n

def _get_edges(data): return data

def _union(i, j, parent, rank, meta):
    root_i = _find(i, parent)
    root_j = _find(j, parent)

    if root_i != root_j:
        if rank[root_i] > rank[root_j]:
            parent[root_j] = root_i
            _merge(root_i, root_j, meta)
        elif rank[root_i] < rank[root_j]:
            parent[root_i] = root_j
            _merge(root_j, root_i, meta)
        else:
            parent[root_j] = root_i
            rank[root_i] += 1
            _merge(root_i, root_j, meta)
        return True
    return False

def _find(i, parent):
    if parent[i] != i:
        parent[i] = _find(parent[i], parent)
    return parent[i]

def _merge(keep_root, drop_root, meta):
    if meta:
        meta[keep_root] += meta[drop_root]

def _update_count(count): return count - 1

def _calc_result(count, meta, metadata):
    if metadata: return max(meta) if meta else 0
    return count
