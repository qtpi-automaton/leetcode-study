**Back (The Answer):**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        # avoid overflow
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # not found (or return left for insertion point)
    return -1

# Search on answer space
def search_answer(lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```
