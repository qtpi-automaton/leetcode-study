**Back (The Answer):**
```python
def sliding_window_template(arr):
    left = 0
    window = {}
    result = INITIAL_VALUE
    
    for right in range(len(arr)):
        # 1. EXPAND
        right_element = arr[right]
        window[right_element] = window.get(right_element, 0) + 1
        
        # 2. SHRINK based on CONDITION
        while CONDITION(window):
            # 3a. Update BEFORE shrinking
                        
            left_element = arr[left]
            window[left_element] -= 1
            if window[left_element] == 0:
                del window[left_element]
            left += 1
        
        # 3b. Update AFTER shrinking
    
    return result
```

**Key insight:** MIN problems update result BEFORE shrinking (while valid), MAX problems update result AFTER shrinking (while invalid).
