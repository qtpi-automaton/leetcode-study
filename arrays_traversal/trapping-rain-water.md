**

***********************

42. Trapping Rain Water

***********************

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Â 

Example 1:

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZwAAAChCAYAAADz0gn+AAAQAElEQVR4AeydC5RdVZnn/9+5tyovEkhCHgaFKMSILUsc56HO2LZLW7RtIBDRbmZJN6tdJsRBZ+lazqi00KHXGteMOqiERKRVUGHRjcFEFAcRAiIooIAKIQaBBJJUmWelkkqlUvfs+X/73Ft1U6nK855z6/E/Od/e++yzz/72/u3Hd/Y+N0kSdIiACIiACIhAAQQS6BABERABERCBAgjI4BQAWSpGKAEVWwREoKEEZHAailOZiYAIiIAIDEVABmcoMooXAREQAREYisBxxcvgHBc2PSQCIiACInCsBBpqcNKQHqt+pRcBERABERgjBBpqcBJLEEKIMkb4qZojhICKKQIi0HwCDTM4lUoFO3bsiMbGzJpfM5VABERABERgWBE4YYMTqttoW7ZswfLly7F79+5YwVp8vJAjAiIgAiIwTAkUV6wTMjiB22fGbTQv7sMPP4yrrroKTz31lF9ypQNKiGE5IiACIiACInDCBscRtre343vf+54HsXLlSnR2diJJEqSpfkQQocgRAREQARHAcRscX924UXGGa9aswerVqz2Ir371q3j88cdj2My0yokk5DSQgLISAREYoQROyOB4ndva2nDzzTd7EOeee270fZXj33LcIGmVE5HIEQEREIExT+C4DE796uahhx7C3XffjcmTJ2P79u0R6PXXX48nn3wyhs20yokg5IiACIhA3gSGef7HbXC8Xhs2bMAll1ziwfjNxg1OuVyO19dddx22bdsW491AxUg5IiACIiACY5bAcRkcs+zv2XR0dGDZsmVYsWIF3vzmN6OrqwsLFy7EN77xDZx33nl9P5E2y9KPWcqquAiIgAiIwPH9aMAs2yZ7wxvegCVLluAjH/kIzjnnnIjzLW95S7xetGgR5s6dG380YCaDE+HIGUBAlyIgAmOJwHGtcByQmcXtMvDwf2Wgtm1W/yMB/9GAmYwNEekUAREQgTFP4LgNjpOrGZeasfG4ocJ+TyICIiACInB0BEZjqhMyOGaHrl7MDo0bjeBUJxEQAREQgWMjcEIG59hUKbUIiIAIiMBYJiCDM5Zbv5F1V14iIAIicAQCMjhHAKTbIiACIiACjSEgg9MYjspFBERABIYioPgqARmcKgh5IiACIiAC+RKQwcmXr3IXAREQARGo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)

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]

Output: 9

Â 

Constraints:

- n == height.length

- 1 <= n <= 2 * 104

0 <= height[i] <= 105**







### Approach 1: Brute force

#### Intuition

Do as directed in question. For each element in the array, we find the maximum level of water it can trap after the rain, which is equal to the minimum of maximum height of bars on both the sides minus its own height.

#### Algorithm

- Initialize ans=0
- Iterate the array from left to right:
  - Initialize left_max=0 and right_max=0
  - Iterate from the current element to the beginning of array updating:
    - left_max=max(left_max,height[j])
  - Iterate from the current element to the end of array updating:
    - right_max=max(right_max,height[j])
  - Add min(left_max,right_max)−height[i] to ans

#### Implementation

#### Complexity Analysis

- Time complexity: O(n2). For each element of array, we iterate the left and right parts.

- Space complexity: O(1) extra space.

---

### Approach 2: Dynamic Programming

#### Intuition

In brute force, we iterate over the left and right parts again and again just to find the highest bar size upto that index. But, this could be stored. Voila, dynamic programming.

The concept is illustrated as shown:

![Dynamic programming](https://leetcode.com/problems/trapping-rain-water/solutions/127551/Figures/42/trapping_rain_water_fix.png)

#### Algorithm

- Find maximum height of bar from the left end upto an index i in the array left_max.
- Find maximum height of bar from the right end upto an index i in the array right_max.
- Iterate over the height array and update ans:
  - Add min(left_max[i],right_max[i])−height[i] to ans

#### Implementation





class Solution:
    def trap(self, height: List[int]) -> int:
        # Case of empty height list
        if len(height) == 0:
            return 0
        ans = 0
        size = len(height)
        # Create left and right max arrays
        left_max, right_max = [0] * size, [0] * size
        # Initialize first height into left max
        left_max[0] = height[0]
        for i in range(1, size):
            # update left max with current max
            left_max[i] = max(height[i], left_max[i - 1])
        # Initialize last height into right max
        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            # update right max with current max
            right_max[i] = max(height[i], right_max[i + 1])
        # Calculate the trapped water
        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]
        # Return amount of trapped water
        return ans







#### Complexity Analysis

- Time complexity: O(n).
  
  - We store the maximum heights upto a point using 2 iterations of O(n) each.
  - We finally update ans using the stored values in O(n).

- Space complexity: O(n) extra space.
  
  - Additional O(n) space for left_max and right_max arrays than in [Approach 1](https://leetcode.com/problems/trapping-rain-water/solutions/127551/trapping-rain-water-by-leetcode-27de/#approach-1-brute-force).

---

### Approach 3: Using stacks

#### Intuition

Instead of storing the largest bar upto an index as in [Approach 2](https://leetcode.com/problems/trapping-rain-water/solutions/127551/trapping-rain-water-by-leetcode-27de/#approach-2-dynamic-programming), we can use stack to keep track of the bars that are bounded by longer bars and hence, may store water. Using the stack, we can do the calculations in only one iteration.

We keep a stack and iterate over the array. We add the index of the bar to the stack if bar is smaller than or equal to the bar at top of stack, which means that the current bar is bounded by the previous bar in the stack. If we found a bar longer than that at the top, we are sure that the bar at the top of the stack is bounded by the current bar and a previous bar in the stack, hence, we can pop it and add resulting trapped water to ans.

#### Algorithm

- Use stack to store the indices of the bars.
- Iterate the array:
  - While stack is not empty and height[current]>height[st.top()]
    - It means that the stack element can be popped. Pop the top element as top.
    - Find the distance between the current element and the element at top of stack, which is to be filled.  
      distance=current−st.top()−1
    - Find the bounded height  
      bounded_height=min(height[current],height[st.top()])−height[top]
    - Add resulting trapped water to answer ans+=distance×bounded_height
  - Push current index to top of the stack
  - Move current to the next position

#### Implementation





class Solution:
    def trap(self, height):
        ans = 0
        current = 0
        st = []
        while current < len(height):
            while len(st) != 0 and height[current] > height[st[-1]]:
                top = st[-1]
                st.pop()
                if len(st) == 0:
                    break
                distance = current - st[-1] - 1
                bounded_height = (
                    min(height[current], height[st[-1]]) - height[top]
                )
                ans += distance * bounded_height
            st.append(current)
            current += 1
        return ans







#### Complexity Analysis

- Time complexity: O(n).
  - Single iteration of O(n) in which each bar can be touched at most twice(due to insertion and deletion from stack) and insertion and deletion from stack takes O(1) time.
- Space complexity: O(n). Stack can take upto O(n) space in case of stairs-like or flat structure.

---

### Approach 4: Using 2 pointers

#### Intuition

As in [Approach 2](https://leetcode.com/problems/trapping-rain-water/solutions/127551/trapping-rain-water-by-leetcode-27de/#approach-2-dynamic-programming), instead of computing the left and right parts separately, we may think of some way to do it in one iteration.  
From the figure in dynamic programming approach, notice that as long as right_max[i]>left_max[i] (from element 0 to 6), the water trapped depends upon the left_max, and similar is the case when left_max[i]>right_max[i] (from element 8 to 11).  
So, we can say that if there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction (from left to right). As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left).  
We must maintain left_max and right_max during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.

#### Algorithm

- Initialize left pointer to 0 and right pointer to size-1
- While left<right, do:
  - If height[left] is smaller than height[right]
    - If height[left]≥left_max, update left_max
    - Else add left_max−height[left] to ans
    - Add 1 to left.
  - Else
    - If height[right]≥right_max, update right_max
    - Else add right_max−height[right] to ans
    - Subtract 1 from right.

Refer to the example for better understanding:  

#### Implementation



class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans





#### Complexity Analysis

- Time complexity: O(n). Single iteration of O(n).
- Space complexity: O(1) extra space. Only constant space required for left, right, left_max and right_max.
