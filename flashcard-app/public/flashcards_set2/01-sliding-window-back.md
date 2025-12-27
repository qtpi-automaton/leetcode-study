**Back (The Answer):**
```python
def sliding_window(arr):
    left = 0
    result = 0  # or float('inf') for minimum
    window_state = {}  # track window contents
    
    for right in range(len(arr)):
        # 1. EXPAND: add arr[right] to window
        window_state[arr[right]] = window_state.get(arr[right], 0) + 1
        
        # 2. SHRINK: while window invalid, remove from left
        while not is_valid(window_state):
            window_state[arr[left]] -= 1
            left += 1
        
        # 3. UPDATE: record result if valid
        result = max(result, right - left + 1)
    
    return result
```
