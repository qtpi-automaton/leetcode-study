**Back (The Answer):**
```python
def two_pointers_template(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # 1. EVALUATE current pair
        score = EVALUATE(arr[left], arr[right])
        
        # 2. CHECK if solution found
        if score == TARGET:
            return RESULT
        
        # 3. MOVE based on comparison
        elif CONDITION(score):
            left += 1
        else:
            right -= 1
    
    return DEFAULT_RESULT
```

**Core idea:** Pointers converge from opposite ends, move one per iteration based on evaluation.
