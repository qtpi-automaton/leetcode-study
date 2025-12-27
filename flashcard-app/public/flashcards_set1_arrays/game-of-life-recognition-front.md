**Front (The Prompt):**
* **Problem:** Apply Conway's Game of Life rules simultaneously to all cells in a grid. Each cell is alive (1) or dead (0). Count 8 neighbors (horizontal, vertical, diagonal).
  * **Rules:**
    * Live cell + <2 neighbors → dies (underpopulation)
    * Live cell + 2-3 neighbors → lives
    * Live cell + >3 neighbors → dies (overpopulation)
    * Dead cell + exactly 3 neighbors → becomes alive (reproduction)
  * All cells update at the same time (can't use updated values mid-iteration)
* **Key Constraints:** m,n ≤ 25, must update in-place simultaneously