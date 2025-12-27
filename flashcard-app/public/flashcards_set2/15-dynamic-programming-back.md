**Back (The Answer):**
```python
# 1D DP (e.g., climbing stairs, house robber)
def dp_1d(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # base case
    
    for i in range(1, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # recurrence
    
    return dp[n]

# 2D DP (e.g., grid paths, LCS, knapsack)
def dp_2d(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]  # base case
    
    for i in range(m):
        for j in range(n):
            # recurrence: dp[i][j] = f(dp[i-1][j], dp[i][j-1], ...)
            pass
    
    return dp[m-1][n-1]

# Space optimization: often can reduce to O(n) using prev row only
```
