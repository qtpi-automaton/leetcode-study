**Back (The Answer):**
```python
def sliding_window(arr):
    left = 0
    # 0 for MAX, float('inf') for MIN
    result = 0
    window = {}

    for right in range(len(arr)):
        # 1. EXPAND: Add arr[right] to window
        window[arr[right]] = window.get(arr[right], 0) + 1

        # 2. SHRINK: While condition met
        # MAX: shrink while INVALID | MIN: shrink while VALID
        while CONDITION(window):
            window[arr[left]] -= 1
            if window[arr[left]] == 0:
                del window[arr[left]]
            left += 1

        # 3. UPDATE result
        result = max(result, right - left + 1)

    return result
```
