**Back (The Answer):**
```python
def dfs(node):
    if not node:
        return

    # PREORDER: process before children
    print(node.val)

    dfs(node.left)
    # INORDER: process between (BST = sorted)
    dfs(node.right)
    # POSTORDER: process after (bottom-up)

def has_path_sum(node, target):
    if not node:
        return False
    if not node.left and not node.right:
        return node.val == target
    target -= node.val
    return has_path_sum(node.left, target) or has_path_sum(node.right, target)
```
