**Back (The Answer):**
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # sort by start
    merged = []
    
    for interval in intervals:
        # if merged empty OR no overlap
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # overlap: extend end of last interval
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged
```
