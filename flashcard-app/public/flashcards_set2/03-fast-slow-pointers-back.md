**Back (The Answer):**
```python
def fast_slow_template(head):
    # 1. INITIALIZE
    slow = fast = head
    
    # 2. MOVE pointers
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # 3a. CHECK during movement (cycle detection)
        if slow == fast:
            return CYCLE_RESULT
    
    # 3b. CHECK after movement (midpoint/end)
    return slow  # or other end-state result
```

**Core idea:** Fast moves 2x speed of slow. When they meet = cycle. When fast ends = slow at middle.
