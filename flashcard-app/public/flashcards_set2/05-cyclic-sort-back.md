**Back (The Answer):**
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct = nums[i] - 1  # where it should be
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    return nums

# After sort: nums[i] != i+1 means i+1 is missing
```
