**Back (The Answer):**
```python
def two_pointers(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        curr = arr[left] + arr[right]

        if curr == target:
            return [left, right]
        elif curr < target:
            # need larger
            left += 1
        else:
            # need smaller
            right -= 1

    return []
```
