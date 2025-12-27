**Back (The Answer):**
```python
def dfs(node):
    if not node:
        return  # base case
    
    # PREORDER: process before children
    print(node.val)
    
    dfs(node.left)
    
    # INORDER: process between children (BST gives sorted)
    # print(node.val)
    
    dfs(node.right)
    
    # POSTORDER: process after children (bottom-up)
    # print(node.val)

# Path sum pattern
def has_path_sum(node, target):
    if not node:
        return False
    if not node.left and not node.right:  # leaf
        return node.val == target
    return (has_path_sum(node.left, target - node.val) or
            has_path_sum(node.right, target - node.val))
```
