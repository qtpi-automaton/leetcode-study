**Back (The Answer):**
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1  # where this number should be
        
        # if not in correct position, swap
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1  # already correct, move on
    
    return nums

# Find missing: after sort, nums[i] != i+1 means i+1 is missing
```
