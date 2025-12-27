**Back (The Answer):**
```python
import heapq

def top_k_largest(nums, k):
    # min-heap of size k
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap

def top_k_smallest(nums, k):
    # max-heap (negate values)
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
        if len(heap) > k:
            heapq.heappop(heap)
    return [-x for x in heap]
```
