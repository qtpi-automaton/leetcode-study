**Back (The Answer):**
```python
def solve_backtracking(nums):
    result = []

    def backtrack(path, start):
        # 1. GOAL: Add valid solutions
        # Subsets: always add | Permutations: len(path) == len(nums)
        result.append(path[:])  # append a COPY

        # 2. CHOICES: Iterate options
        for i in range(start, len(nums)):
            # (Optional) Skip duplicates: if i > start and nums[i] == nums[i-1]: continue

            # 3. CHOOSE
            path.append(nums[i])

            # 4. EXPLORE: i+1 = no reuse, i = reuse allowed
            backtrack(path, i + 1)

            # 5. UN-CHOOSE (backtrack)
            path.pop()

    backtrack([], 0)
    return result
```
