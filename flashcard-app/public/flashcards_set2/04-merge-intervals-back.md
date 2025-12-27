**Back (The Answer):**
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        # no overlap
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # extend end
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
```
