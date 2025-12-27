**Back (The Answer):**
```python
import heapq

def top_k_largest(nums, k):
    # Min-heap of size k (keeps k largest)
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # remove smallest
    
    return heap  # k largest elements

def top_k_smallest(nums, k):
    # Max-heap (negate values)
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
        if len(heap) > k:
            heapq.heappop(heap)
    return [-x for x in heap]

# K most frequent: heap of (freq, elem)
```
