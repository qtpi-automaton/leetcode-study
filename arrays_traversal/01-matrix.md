**

**************

542. 01 Matrix

**************

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Â 

Example 1:

![](data:image/jpeg;base64,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)

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]

Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

![](data:image/jpeg;base64,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)

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]

Output: [[0,0,0],[0,1,0],[1,2,1]]

Â 

Constraints:

- m == mat.length

- n == mat[i].length

- 1 <= m, n <= 104

- 1 <= m * n <= 104

- mat[i][j] is either 0 or 1.

- There is at least one 0 in mat.

**

## Solution

---

### Overview

Whenever you have a matrix where you can move between adjacent cells, you should immediately think about graphs. A matrix is a very common format for a graph to take.

You can treat each square as a node. There are edges between adjacent nodes. Here are some other graph problems that use matrices:

- [Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- [Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
- [Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/)
- [Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/)

---

### Approach 1: Breadth-First Search (BFS)

**Intuition**

The first thing you should think about when it comes to shortest path problems on graphs is BFS. If you're not familiar with BFS, we suggest you read the relevant [LeetCode Explore Card](https://leetcode.com/explore/featured/card/graph/620/breadth-first-search-in-graph/).

First of all, any cell with value `0` does not need to be changed. For a given cell with value `1`, we need to find the nearest `0`. We could perform a BFS starting from the cell and terminate once we find any `0`, as this `0` would be the closest one. By repeating this for every cell with value `1`, we would solve the problem.

The issue with this is that the constraints state that the matrix could have up to `10,000` cells. Think about a matrix where the entire matrix is `1` except for one of the corners. We would need to perform O(size) BFS, with each BFS costing up to O(size). In the worst-case scenario, the number of operations we would need is on the order of `100,000,000`, which would fail the time limit. We need to think of a more efficient way to perform the BFS.

What if we started the BFS from `0` instead of `1`? Let's say that we started a BFS from a `1` and found that the nearest `0` was `x` steps away. Now, let's start a BFS from that `0` until we reach the original `1`. We will again find that the BFS takes `x` steps. Basically, it doesn't matter if we start from the `0` or `1`, both will result in the same distance.

If we start BFS from `1`, we can only find the shortest distance for that `1`. If we start BFS from `0`, we could find the shortest distance for many `1` at a time. So which `0` should we start from? The answer is all of them!

Let's think about how BFS works. From a source node, we first visit all nodes at a distance of `1`. Next, we visit all nodes at a distance of `2`, then `3`, and so on. We can say a node at a distance of x from the source belongs to "level x". So the source is at level 0, the neighbors of the source are at level 1, the neighbors of those nodes are at level 2, and so on.

We are used to starting BFS from only one source node, i.e. level 0 only has one node. But there is nothing stopping us from having multiple nodes in level 0. If we start with multiple nodes in level 0, then the nodes in level 1 will be all the neighbors of the nodes in level 0. The nodes in level 2 will be all the neighbors of the nodes in level 1, and so on - the logic is identical. The following animation illustrates this idea (cells are labeled by their level):

As you can see, we don't need to visit any node more than once, which drastically improves our time complexity.

**Algorithm**

1. Create a copy of `mat`, we'll call it `matrix`.
2. Use a data structure `seen` to mark nodes we have already visited and a `queue` for the BFS.
3. Put all nodes with `0` into the `queue`. We will also track the level/number of steps with each `queue` entry. Mark these nodes in `seen` as well.
4. Perform the BFS:
   - While `queue` is not empty, get the current `row, col, steps` from the `queue`.
   - Iterate over the 4 directions. For each `nextRow, nextCol`, check if it is in bounds and not already visited in `seen`.
   - If so, set `matrix[nextRow][nextCol] = steps + 1` and push `nextRow, nextCol, steps + 1` onto the `queue`. Also mark `nextRow, nextCol` in `seen`.
5. Return `matrix`.

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        matrix = [row[:] for row in mat]
        m = len(matrix)
        n = len(matrix[0])
        queue = deque()
        seen = set()
    
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    queue.append((row, col, 0))
                    seen.add((row, col))
    
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
        while queue:
            row, col, steps = queue.popleft()
    
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if (next_row, next_col) not in seen and valid(next_row, next_col):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
                    matrix[next_row][next_col] = steps + 1
    
        return matrix

**Complexity Analysis**

Given m as the number of rows and n as the number of columns,

- Time complexity: O(m⋅n)
  
  The BFS never visits a node more than once due to `seen`. Each node has at most 4 neighbors, so the work done at each node is O(1). This gives us a time complexity of O(m⋅n), the number of nodes.

- Space complexity: O(m⋅n)
  
  Note: some people may choose to modify the input `mat` instead of creating a copy `matrix` and using `seen`.
  
  It is generally not considered good practice to modify the input, especially if it's an array as they are passed by reference. Even then, you would only be saving on **auxiliary space** - if you modify the input as part of your algorithm, you still need to count it towards the space complexity.
  
  We could also elect to not count `matrix` as part of the space complexity as it serves only as the output and the output does not count towards the space complexity if it is not used in any logic during the algorithm.
  
  There is a lot of nuance when it comes to these decisions and you should always clarify your decisions with the interviewer.
  
  In our implementation, `seen` and `queue` uses O(m⋅n) space regardless of interpretation, so that is our space complexity.

### Approach 2: Dynamic Programming

**Intuition**

Let's say we're currently at `row, col`. What is the minimum distance for this cell? We must have arrived from one of the following:

- `row - 1, col`
- `row + 1, col`
- `row, col - 1`
- `row, col + 1`

Therefore the minimum distance for `row, col` is 1 + the minimum distance from these four neighbors. This gives us a natural recurrence that we can solve using DP:

`dp[row][col] = 1 + min(dp[row - 1][col], dp[row + 1][col], dp[row][col - 1], dp[row][col + 1])`

Where `dp[x][y]` is the minimum distance for the cell `mat[x][y]` and `mat[x][y] != 0`.

The issue with this recurrence is that we don't have an obvious order in which we should iterate over `mat`. We can't just iterate over each cell and check the four directions immediately because the other directions haven't been calculated yet. DP only works with values that have been previously calculated. So how do we calculate `dp`?

Let's pretend that we can only move down and right (not allowed to move up and left). That would change the recurrence. To reach `row, col`, we must have arrived from one of:

- `row - 1, col`
- `row, col - 1`

So the new recurrence would be:

`dp[row][col] = 1 + min(dp[row - 1][col], dp[row][col - 1])`

If we start at the top left and iterate row by row, column by column, we will correctly calculate `dp` for any paths that move down and right. Now, let's pretend that we can only move up and left (not allowed to move down and right). Again, this would change our recurrence:

`dp[row][col] = 1 + min(dp[row + 1][col], dp[row][col + 1])`

If we start at the bottom right and iterate backward, we will correctly calculate `dp` for any paths that move up and left. Finally, `dp` is the answer!

**Click here to see proof of this algorithm's correctness if interested**

Assume we have a 2x2 matrix: `[a, b], [c, d]`. There are two possibilities:

1. `a = 0`. On the first pass (moving down and right only), we can correctly calculate `dp`.
2. `a = 1`. One of `b, c, d` must be `0`, since the constraints say there must be at least one `0`. No matter where the `0` is, we can calculate the correct distance for `d`, since it is in the bottom right. Now that we know the answer for `d`, in the second pass, we can calculate the answer for `b, c`, and with that we can calculate the answer of `a`.

Therefore, `a, b, c, d` can always be calculated regardless of their initial values. This logic extends to any size matrix.

**Algorithm**

1. Create a copy of `mat`, we'll call it `dp`.
2. Iterate row by row, column by column. At each `row, col`:
   - Initialize `minNeighbor` to a large value. This represents the minimum value of `dp` from the cells we could have arrived from.
   - Making sure to stay in bounds, check the two cells we could have arrived from: `row - 1, col` and `row, col - 1`.
   - Update `minNeighbor` with their `dp` values.
   - Set `dp[row][col] = minNeighbor + 1`.
3. Iterate over `dp` again but in reverse order. At each `row, col`:
   - Initialize `minNeighbor` to a large value.
   - Making sure to stay in bounds, check the two cells we could have arrived from: `row + 1, col` and `row, col + 1`.
   - Update `minNeighbor` with their `dp` values.
   - If `minNeighbor + 1` is less than `dp[row][col]` (the minimum distance if we only considered down-right paths), then update it.
4. Return `dp`.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = [row[:] for row in mat]
        m, n = len(dp), len(dp[0])

        for row in range(m):
            for col in range(n):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row > 0:
                        min_neighbor = min(min_neighbor, dp[row - 1][col])
                    if col > 0:
                        min_neighbor = min(min_neighbor, dp[row][col - 1])
    
                    dp[row][col] = min_neighbor + 1
    
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row < m - 1:
                        min_neighbor = min(min_neighbor, dp[row + 1][col])
                    if col < n - 1:
                        min_neighbor = min(min_neighbor, dp[row][col + 1])
    
                    dp[row][col] = min(dp[row][col], min_neighbor + 1)
    
        return dp

**Complexity Analysis**

Given m as the number of rows and n as the number of columns,

- Time complexity: O(m⋅n)
  
  We iterate over m⋅n cells twice, performing constant work at each iteration.

- Space complexity: O(m⋅n)
  
  As discussed above, some people may choose to reuse `mat` as `dp`.
  
  A common misconception is that it would be O(1) space. It would only be O(1) **auxiliary space**, but as we are modifying the input and using it in the algorithm, it must be included in the space complexity. Again, it is not considered good practice to modify the input anyways, which is why we are creating `dp`, which uses O(m⋅n) space.
