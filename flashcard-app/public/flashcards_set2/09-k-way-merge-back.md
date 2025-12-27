**Back (The Answer):**
```python
import heapq

def merge_k_sorted(lists):
    # (value, list_idx, elem_idx)
    heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, li, ei = heapq.heappop(heap)
        result.append(val)

        if ei + 1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][ei + 1], li, ei + 1))

    return result
```
