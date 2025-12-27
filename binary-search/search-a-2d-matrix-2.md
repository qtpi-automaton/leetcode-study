## Solution

---

### Approach 1: Brute Force

**Intuition**

As a baseline, we can search the 2D array the same way we might search an  
unsorted 1D array -- by examining each element.

**Algorithm**

The algorithm doesn't really do anything more clever than what is explained  
by the intuition; we loop over the array, checking each element in turn. If  
we find it, we return `true`. Otherwise, if we reach the end of the nested  
`for` loop without returning, we return `false`. The algorithm must return  
the correct answer in all cases because we exhaust the entire search space.





class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True

        return False





**Complexity Analysis**

- Time complexity : O(nm)
  
  Becase we perform a constant time operation for each element of an  
  n×m element matrix, the overall time complexity is equal to the  
  size of the matrix.

- Space complexity : O(1)
  
  The brute force approach does not allocate more additional space than a  
  handful of pointers, so the memory footprint is constant.





### Approach 2: Binary Search

**Intuition**

The fact that the matrix is sorted suggests that there must be some way to use  
binary search to speed up our algorithm.

**Algorithm**

First, we ensure that `matrix` is not `null` and not empty. Then, if we  
iterate over the matrix diagonals, we can maintain an invariant that the  
slice of the row and column beginning at the current (row,col) pair is  
sorted. Therefore, we can always binary search these row and column slices  
for `target`. We proceed in a logical fashion, iterating over the diagonals,  
binary searching the rows and columns until we either run out of diagonals  
(meaning we can return `False`) or find `target` (meaning we can return  
`True`). The `binarySearch` function works just like normal binary search,  
but is made ugly by the need to search both rows and columns of a  
two-dimensional array.



class Solution:
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while hi >= lo:
            mid = (lo + hi) // 2
            if vertical: # searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else: # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
    
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False
    
        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
    
        return False





**Complexity Analysis**

- Time complexity : O(log(n!))
  
  It's not super obvious how O(log(n!)) time complexity arises  
  from this algorithm, so let's analyze it step-by-step. The  
  asymptotically-largest amount of work performed is in the main loop,  
  which runs for min(m,n) iterations, where m denotes the number  
  of rows and n denotes the number of columns. On each iteration, we  
  perform two binary searches on array slices of length m−i and  
  n−i. Therefore, each iteration of the loop runs in  
  O(log(m−i)+log(n−i)) time, where i denotes the current  
  iteration. We can simplify this to O(2⋅log(n−i))=O(log(n−i))  
  by seeing that, in the worst case, n≈m. To see why, consider  
  what happens when n≪m (without loss of generality); n will  
  dominate m in the asymptotic analysis. By summing the runtimes of all  
  iterations, we get the following expression:
  
  (1)O(log(n)+log(n−1)+log(n−2)+…+log(1))
  
  Then, we can leverage the log multiplication rule (log(a)+log(b)=log(ab))  
  to rewrite the complexity as:
  
  (2)O(log(n)+log(n−1)+log(n−2)+…+log(1))​=O(log(n⋅(n−1)⋅(n−2)⋅…⋅1))=O(log(1⋅…⋅(n−2)⋅(n−1)⋅n))=O(log(n!))​
  
  Because this time complexity is fairly uncommon, it is worth thinking about  
  its relation to the usual analyses. For one, log(n!)=O(nlogn).  
  To see why, recall step 1 from the analysis above; there are n terms, each no  
  greater than log(n). Therefore, the asymptotic runtime is certainly no worse than  
  that of an O(nlogn) algorithm.

- Space complexity : O(1)
  
  Because our binary search implementation does not literally slice out  
  copies of rows and columns from `matrix`, we can avoid allocating  
  greater-than-constant memory.

---

### Approach 3: Divide and Conquer

**Intuition**

We can partition a sorted two-dimensional matrix into four sorted submatrices,  
two of which might contain `target` and two of which definitely do not.

**Algorithm**

Because this algorithm operates recursively, its correctness can be asserted  
via the correctness of its base and recursive cases.

*Base Case*

For a sorted two-dimensional array, there are two ways to determine in  
constant time whether an arbitrary element `target` can appear in it. First,  
if the array has zero area, it contains no elements and therefore cannot  
contain `target`. Second, if `target` is smaller than the array's smallest  
element (found in the top-left corner) or larger than the array's largest  
element (found in the bottom-right corner), then it definitely is not  
present.

*Recursive Case*

If the base case conditions have not been met, then the array has positive  
area and `target` could potentially be present. Therefore, we seek along the  
matrix's middle column for an index `row` such that  
matrix[row−1][mid]<target<matrix[row][mid] (obviously, if we find  
`target` during this process, we immediately return `true`). The existing  
matrix can be partitioned into four submatrice around this index; the  
top-left and bottom-right submatrice cannot contain `target` (via the  
argument outlined in *Base Case* section), so we can prune them from the  
search space. Additionally, the bottom-left and top-right submatrice are  
sorted two-dimensional matrices, so we can recursively apply this algorithm  
to them.



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
    
            mid = left + (right-left) // 2
    
            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
    
            return search_rec(left, row, mid - 1, down) or \
                   search_rec(mid + 1, up, right, row - 1)
    
        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)





**Complexity Analysis**

- Time complexity : O(nlogn)
  
  First, for ease of analysis, assume that n≈m, as in the  
  analysis of approach 2. Also, assign x=n2=∣matrix∣; this will make  
  the [master method](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))  
  easier to apply. Now, let's model the runtime of the  
  divide & conquer approach as a recurrence relation:
  
  T(x)=2⋅T(4x​)+x​
  
  The first term (2⋅T(4x​)) arises from the fact that we  
  recurse on two submatrices of roughly one-quarter size, while  
  x​ comes from the time spent seeking along a O(n)-length  
  column for the partition point. After binding the master method variables  
  (a=2;b=4;c=0.5) we notice that logb​a=c. Therefore, this  
  recurrence falls under case 2 of the master method, and the following  
  falls out:
  
  T(x)​=O(xc⋅logx)=O(x0.5⋅logx)=O((n2)0.5⋅log(n2))=O(n⋅log(n2))=O(2n⋅logn)=O(n⋅logn)​
  
  Extension: what would happen to the complexity if we binary searched for  
  the partition point, rather than used a linear scan?

- Space complexity : O(logn)
  
  Although this approach does not fundamentally require  
  greater-than-constant addition memory, its use of recursion means that it  
  will use memory proportional to the height of its recursion tree. Because  
  this approach discards half of `matrix` on each level of recursion (and  
  makes two recursive calls), the height of the tree is bounded by logn.

---

### Approach 4: Search Space Reduction

**Intuition**

Because the rows and columns of the matrix are sorted (from left-to-right and  
top-to-bottom, respectively), we can prune O(m) or  
O(n) elements when looking at any particular value.

**Algorithm**

First, we initialize a (row,col) pointer to the bottom-left of the  
matrix.[1](https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/127690/search-a-2d-matrix-ii-by-leetcode-zw5h/#user-content-fn-1) Then, until we find `target` and return `true` (or the pointer  
points to a (row,col) that lies outside of the dimensions of the  
matrix), we do the following: if the currently-pointed-to value is larger  
than `target` we can move one row "up". Otherwise, if the  
currently-pointed-to value is smaller than `target`, we can move one column  
"right". It is not too tricky to see why doing this will never prune the  
correct answer; because the rows are sorted from left-to-right, we know that  
every value to the right of the current value is larger. Therefore, if the  
current value is already larger than `target`, we know that every value to  
its right will also be too large. A very similar argument can be made for the  
columns, so this manner of search will always find `target` in the matrix (if  
it is present).

Check out some sample runs of the algorithm in the animation below:



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])
    
        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0
    
        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
    
        return False





**Complexity Analysis**

- Time complexity : O(n+m)
  
  The key to the time complexity analysis is noticing that, on every  
  iteration (during which we do not return `true`) either `row` or `col` is  
  is decremented/incremented exactly once. Because `row` can only be  
  decremented m times and `col` can only be incremented n times  
  before causing the `while` loop to terminate, the loop cannot run for  
  more than n+m iterations. Because all other work is constant, the  
  overall time complexity is linear in the sum of the dimensions of the  
  matrix.

- Space complexity : O(1)
  
  Because this approach only manipulates a few pointers, its memory  
  footprint is constant.

- ### Footnotes
  
  ## Footnotes
  
  1. This would work equally well with a pointer initialized to the  
     top-right. Neither of the other two corners would work, as pruning a  
     row/column might prevent us from achieving the correct answer. [↩](https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/127690/search-a-2d-matrix-ii-by-leetcode-zw5h/#user-content-fnref-1)
