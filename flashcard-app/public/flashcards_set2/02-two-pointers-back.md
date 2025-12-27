**Back (The Answer):**
```python
def two_pointers(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current = arr[left] + arr[right]
        
        if current == target:
            return [left, right]  # found
        elif current < target:
            left += 1   # need larger sum
        else:
            right -= 1  # need smaller sum
    
    return []  # not found
```
