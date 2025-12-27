**Back (The Answer):**
```python
def has_cycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next       # move 1 step
        fast = fast.next.next  # move 2 steps
        
        if slow == fast:
            return True  # cycle detected
    
    return False  # no cycle

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # middle node
```
