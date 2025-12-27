**

***************************

419. Battleships in a Board

***************************

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Â 

Example 1:

![](data:image/jpeg;base64,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)

Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

Output: 2

Example 2:

Input: board = [["."]]

Output: 0

Â 

Constraints:

- m == board.length

- n == board[i].length

- 1 <= m, n <= 200

- board[i][j] is either '.' or 'X'.

Â 

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?

**





## Intuition

When we first look at this problem, the natural instinct is to use DFS to explore each battleship as a connected component. We'd start from an unvisited `'X'` cell, traverse all connected `'X'` cells to mark the entire battleship as visited, then increment our count. This is the standard connected components approach.

However, there's a clever observation that makes this problem much simpler: **we don't actually need to traverse the entire battleship**.

Think about it - if battleships can only be straight lines (horizontal or vertical) and they can't touch each other, then each battleship has a unique "starting point". For consistency, let's define this starting point as the **top-left corner** of each battleship:

- For a horizontal battleship, it's the leftmost cell
- For a vertical battleship, it's the topmost cell
- For a single cell battleship, it's that cell itself

The key insight is: **a cell is a starting point if and only if it contains `'X'` AND has no `'X'` above it AND has no `'X'` to its left**.

Why does this work? Because:

1. Every battleship has exactly one starting point (its top-left cell)
2. No non-starting cell can satisfy our condition (it would have an `'X'` either above or to its left)
3. The separation rule guarantees battleships don't touch, so we don't need to worry about distinguishing between different battleships

This transforms our problem from "explore all connected components using DFS" to "count all starting points with a simple scan". We iterate through the matrix once, and for each `'X'` cell at position `(i, j)`, we check:

- Is `board[i-1][j]` (cell above) an `'X'`? If yes, skip - this is not a starting point
- Is `board[i][j-1]` (cell to the left) an `'X'`? If yes, skip - this is not a starting point
- Otherwise, we found a starting point - increment the counter

This approach is elegant because it leverages the problem's constraints (battleships are straight lines and don't touch) to avoid the complexity of DFS traversal entirely. We're essentially counting "heads" of battleships rather than exploring their entire "bodies".





```python
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """
        Count the number of battleships on the board.

        Strategy: Count only the top-left corner of each battleship.
        A cell is considered a battleship's top-left corner if:
        1. It contains 'X'
        2. No 'X' exists directly above it (or it's in the first row)
        3. No 'X' exists directly to its left (or it's in the first column)

        Args:
            board: 2D grid where 'X' represents a battleship part and '.' represents empty water

        Returns:
            Number of battleships on the board
        """
        # Get board dimensions
        rows, cols = len(board), len(board[0])

        # Initialize battleship counter
        battleship_count = 0

        # Iterate through each cell in the board
        for row in range(rows):
            for col in range(cols):
                # Skip empty water cells
                if board[row][col] == '.':
                    continue

                # Skip if this 'X' is part of a battleship that starts above
                # (i.e., not the topmost cell of a vertical battleship)
                if row > 0 and board[row - 1][col] == 'X':
                    continue

                # Skip if this 'X' is part of a battleship that starts to the left
                # (i.e., not the leftmost cell of a horizontal battleship)
                if col > 0 and board[row][col - 1] == 'X':
                    continue

                # This cell is the top-left corner of a battleship
                battleship_count += 1

        return battleship_count
```






