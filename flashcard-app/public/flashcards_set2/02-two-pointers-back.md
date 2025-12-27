**Back (The Answer):**
```python
def two_pointers(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        curr = arr[left] + arr[right]

        if curr == target:
            return [left, right]
        elif curr < target:
            left += 1   # need larger
        else:
            right -= 1  # need smaller

    return []
```
