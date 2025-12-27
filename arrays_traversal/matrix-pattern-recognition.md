# Matrix Problems: Graph vs Two Pointers

## Default: Assume Graph DFS/BFS
For any matrix problem involving:
- Counting regions/components (islands, battleships)
- Spreading/propagation (rotting oranges, flood fill)
- Reachability or shortest path
- Connected cells (4-dir or 8-dir adjacency)

**Graph works. Always.** O(m·n) time, O(m·n) space.

---

## Look for Two Pointer Upgrades
Ask: "Can I avoid exploration because of a constraint?"

| Upgrade Signal | Example | Why It Works |
|----------------|---------|--------------|
| Fixed traversal pattern | Spiral Matrix, Diagonal Traverse | Order is predetermined, just walk it |
| Simple shapes + no touching | Battleships | Only count "top-left corners" — no flood fill needed |
| Answer depends on boundaries | Trapping Rain Water | Global max heights, not neighbor exploration |
| In-place marking with known structure | Set Matrix Zeroes | Use first row/col as markers, scan twice |

**Two Pointers payoff:** O(1) space, cleaner code, shows deeper understanding.

---

## Quick Decision Flow
```
Matrix problem?
  ↓
Could I solve with DFS/BFS? (usually yes)
  ↓
Check constraints:
  - Is traversal order fixed/predictable?
  - Are shapes simple (lines, no weird blobs)?
  - Do components not touch?
  - Does answer depend on global info (boundaries, maxes)?
  ↓
YES to any → Try Two Pointers
NO to all  → Stick with Graph
```

---

## BFS vs DFS
- **"Shortest/minimum"** → BFS (required) — first arrival = shortest path
- **Everything else** → either works, DFS is less code

---

## The One-Liner
**Graph = "discover structure locally"**  
**Two Pointers = "structure is already known globally"**
