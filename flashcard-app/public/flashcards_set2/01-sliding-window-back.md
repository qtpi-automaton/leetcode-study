**Back (The Answer):**
```python
def sliding_window(arr):
    left = 0
    # MAX: result = 0 | MIN: result = float('inf')
    result = 0
    window = {}

    for right in range(len(arr)):
        # EXPAND
        window[arr[right]] = window.get(arr[right], 0) + 1

        # SHRINK: MAX = while INVALID | MIN = while VALID
        while CONDITION(window):
            # MIN only: result = min(result, right - left + 1)
            window[arr[left]] -= 1
            if window[arr[left]] == 0:
                del window[arr[left]]
            left += 1

        # MAX only: result = max(result, right - left + 1)

    return result
```
