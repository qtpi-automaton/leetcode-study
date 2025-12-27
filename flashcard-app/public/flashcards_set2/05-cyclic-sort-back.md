**Back (The Answer):**
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        # where this number should be
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    return nums

# After sort: nums[i] != i+1 means i+1 is missing
```
