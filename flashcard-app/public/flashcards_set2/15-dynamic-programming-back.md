**Back (The Answer):**
```python
# 1D DP
def dp_1d(n):
    # base case
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        # recurrence
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# 2D DP
def dp_2d(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    for i in range(m):
        for j in range(n):
            # dp[i][j] = f(dp[i-1][j], dp[i][j-1])
            pass

    return dp[m-1][n-1]

# Space optimize: use prev row only for O(n) space
```
