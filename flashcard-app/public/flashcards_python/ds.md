### 1. The "Safe" Data Structures (Review)

| Type | Action | Safe Code | Note |
| --- | --- | --- | --- |
| **List** | Add | `arr.append(x)` | - |
| **List** | Remove | `if arr: arr.pop()` | **Must check `if` first!** |
| **List** | Sort | `arr.sort()` | In-place (changes original). |
| **Set** | Add | `s.add(x)` | Not `append`! |
| **Set** | Remove | `s.discard(x)` | Safe (no crash if missing). |
| **Dict** | Read | `d.get(k, -1)` | Safe (returns -1 if missing). |
| **Dict** | Build | `defaultdict(list)` | Auto-creates lists. |
| **String** | Find | `s.find("x")` | Returns `-1` if missing. |
| **Queue** | Pop | `q.popleft()` | Requires `deque`. |
| **Heap** | Pop | `heapq.heappop(h)` | Removes Min. |

---

### 2. The "Math & Numbers" (Essential)

You will need these for finding minimums, maximums, and bounds.

| Goal | Code | Use Case |
| --- | --- | --- |
| **Infinity** | `float('inf')` | Init min/max variables. |
| **Compare** | `max(a, b)` / `min(a, b)` | Updating "best so far". |
| **Absolute** | `abs(a - b)` | Distances. |
| **Power** | `pow(2, 3)` | . |
| **Division** | `5 // 2` | **Integer** division (returns 2). |
| **Modulo** | `5 % 2` | Remainder (returns 1). |

---

### 3. The "Looping" Helpers (Write Clean Code)

Don't write C-style loops (`i = 0; while i < len...`). Use these Pythonic tools.

| Goal | Code | Why |
| --- | --- | --- |
| **Index & Val** | `for i, x in enumerate(arr):` | Gives you both index and item. |
| **Range** | `range(n)` | Loops 0 to n-1. |
| **Reverse** | `range(n-1, -1, -1)` | Loops backwards. |
| **Two Lists** | `for a, b in zip(A, B):` | Loops two arrays at once. |

---

### 4. The "Type Casters" (Conversion)

You often need to switch between types (e.g., Number to String).

| Goal | Code | Example |
| --- | --- | --- |
| **To String** | `str(123)` | `"123"` |
| **To Int** | `int("123")` | `123` |
| **To List** | `list("abc")` | `['a', 'b', 'c']` |
| **To Set** | `set([1, 1, 2])` | `{1, 2}` (Removes duplicates!) |

---

### The "Boilerplate" Blocks (Memorize These Chunks)

**1. The 2D Grid Setup**
*Every Island/Maze problem starts here.*

```python
rows = len(grid)
cols = len(grid[0])

```

**2. The Infinity Setup**
*Every "Find Min/Max Path" problem starts here.*

```python
min_val = float('inf')
max_val = float('-inf')

```

**3. The "Safe Pop" Pattern**
*Every time you pop from a Stack/Queue/Heap.*

```python
if stack:
    item = stack.pop()

```
