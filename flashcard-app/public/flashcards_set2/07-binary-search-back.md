**Back (The Answer):**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # not found (or return left for insertion point)

# Search on answer: binary search on result space
def search_on_answer(lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid      # try smaller
        else:
            lo = mid + 1  # need larger
    return lo
```
