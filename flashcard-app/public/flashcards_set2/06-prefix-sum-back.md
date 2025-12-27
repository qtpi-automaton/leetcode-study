**Back (The Answer):**
```python
def build_prefix(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    return prefix

# O(1) range query
def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]

# Subarray sum equals K
def subarray_sum(nums, k):
    count, curr = 0, 0
    seen = {0: 1}

    for num in nums:
        curr += num
        count += seen.get(curr - k, 0)
        seen[curr] = seen.get(curr, 0) + 1

    return count
```
