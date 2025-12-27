**Back (The Answer):**
```python
import heapq

def top_k_largest(nums, k):
    heap = []  # min-heap of size k
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap

def top_k_smallest(nums, k):
    heap = []  # max-heap (negate values)
    for num in nums:
        heapq.heappush(heap, -num)
        if len(heap) > k:
            heapq.heappop(heap)
    return [-x for x in heap]
```
