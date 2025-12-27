**Back (The Answer):**
```python
def build_prefix_sum(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    return prefix

def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]  # O(1) query

# Subarray sum equals K: use hashmap
def subarray_sum_k(nums, k):
    count = 0
    curr_sum = 0
    prefix_counts = {0: 1}  # sum -> frequency
    
    for num in nums:
        curr_sum += num
        count += prefix_counts.get(curr_sum - k, 0)
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
    
    return count
```
