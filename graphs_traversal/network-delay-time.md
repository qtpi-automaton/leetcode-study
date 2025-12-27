**

***********************

743. Network Delay Time

***********************

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Â 

Example 1:

![](data:image/png;base64,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)

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2

Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1

Output: 1

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2

Output: -1

Â 

Constraints:

- 1 <= k <= n <= 100

- 1 <= times.length <= 6000

- times[i].length == 3

- 1 <= ui, vi <= n

- ui != vi

- 0 <= wi <= 100

- All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

**

## Solution

---

### Overview

We have a network consisting of some nodes and directed edges. Each edge has three components: source, destination, and time. The time of an edge denotes the time it takes for a signal to travel from the source node to the destination node. A signal sent from node k will travel along the edges and will reach some or all the nodes in the network. Our goal is to determine how much time the signal takes to reach every node in the network. If the signal cannot reach every node, we will return `-1`.

It is possible for a node to receive signals from multiple adjacent nodes at different times. The figure below shows that node `a` receives signals from node `k` and node `b` at timestamps `1` and `2`, respectively. The two signals are identical; hence, the timestamp at which a node receives the signal is the time that the first signal reaches the node. In the following example, the time required for node `a` to receive the signal will be `1` unit as this is the first signal to reach node `a`.

![fig](https://leetcode.com/problems/network-delay-time/solutions/1744861/Figures/743/743A.png)

Therefore, the problem boils down to finding the time required for each node to receive the signal, and the answer will be the maximum time required by any of the nodes. Why maximum? Because we need to find the time at which all nodes receive the signal, so the timestamp at which the last node receives the signal is the answer.  

---

### Approach 1: Depth-First Search (DFS)

**Intuition**

> If you're not familiar with DFS, check out our [Graph Explore Card](https://leetcode.com/explore/featured/card/graph/619/depth-first-search-in-graph/).

In this approach, we will simulate the signal and send it through the nodes as per the problem description to find the answer. Starting from node k, the signal will travel to the adjacent nodes along the directed edges. We will track the signal movement with respect to time in a Depth-First Search manner.

Start the DFS with node `currNode = k` and current timestamp `currTime = 0`. Before we traverse to the adjacent we mark the time required for the `currNode` in the array `signalReceivedAt` as `currTime` (`signalReceivedAt[currNode] = currTime]`). Now we will traverse all the adjacent nodes to the `currNode`. For each adjacent node, we will start a DFS with the updated timestamp i.e., equal to the sum of `currTime` and the time it takes to traverse the edge from `currNode` to the adjacent node.

As we discussed before, there can be multiple signals received at a particular node and we are only interested in the time that the first signal reached the node. Hence, we will perform the DFS only if the `currTime` is less than the time we have stored corresponding to `currNode` in `signalReceivedAt`. This is because if the `currTime` is greater than or equal to `signalReceivedAt[currNode]`, it means that `currNode` received a signal before the current signal could reach it.

There is a trick that can reduce the execution time. Instead of traversing adjacent nodes arbitrarily, we can traverse them in increasing order of their travel time. Although this will increase the time complexity of the algorithm, it will increase the probability of finding the fastest time path first. Hence there could be fewer DFS calls and hence better execution time. The below slideshow demonstrates the algorithm.

**Algorithm**

1. Create an adjacency list such that `adj[source]` contains all destination nodes (`dest`) that the signal can travel to from the source node (`source`). For each destination node, there will be a pair `(time, dest)`. Here, `time` denotes the time required for the signal to travel from `source` to `dest`.
2. Sort the edges connecting to every node in `adj` in increasing order of their travel time.
3. For all nodes, initialize `signalReceivedAt` as a large value to signify that, so far, no signal has been received.
4. Perform DFS on the node `currNode` as k and with the `currTime` as `0`. For each recursive call:
   - If the `currTime` is greater than or equal to `signalReceivedAt[currNode]` then return.
   - Otherwise, set `signalReceivedAt[currNode]` equal to `currTime` which is the new shortest time required to reach `currNode`. Then, perform a DFS for each of the adjacent nodes using the updated timestamp.
5. Find the maximum value in the array `signalReceivedAt`. If any value in `signalReceivedAt` is still the large value we initialized the array with, then return -1 as that node is not reachable from `k`. Otherwise, return the maximum value in the array.

**Implementation**

class Solution {
public:
    // Adjacency list, defined it as per the maximum number of nodes
    // But can be defined with the input size as well
    vector<pair<int, int>> adj[101];

    void DFS(vector<int>& signalReceivedAt, int currNode, int currTime) {
        // If the current time is greater than or equal to the fastest signal received
        // Then no need to iterate over adjacent nodes
        if (currTime >= signalReceivedAt[currNode]) {
            return;
        }
    
        // Fastest signal time for currNode so far
        signalReceivedAt[currNode] = currTime;
    
        // Broadcast the signal to adjacent nodes
        for (pair<int, int> edge : adj[currNode]) {
            int travelTime = edge.first;
            int neighborNode = edge.second;
    
            // currTime + time : time when signal reaches neighborNode
            DFS(signalReceivedAt, neighborNode, currTime + travelTime);
        }
    }
    
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Build the adjacency list
        for (vector<int> time : times) {
            int source = time[0];
            int dest = time[1];
            int travelTime = time[2];
    
            adj[source].push_back({travelTime, dest});
        }
    
        // Sort the edges connecting to every node
        for (int i = 1; i <= n; i++) {
            sort(adj[i].begin(), adj[i].end());
        }
    
        vector<int> signalReceivedAt(n + 1, INT_MAX);
        DFS(signalReceivedAt, k, 0);
    
        int answer = INT_MIN;
        for (int node = 1; node <= n; node++) {
            answer = max(answer, signalReceivedAt[node]);
        }
    
        // INT_MAX signifies atleat one node is unreachable
        return answer == INT_MAX ? -1 : answer;
    }

};

**Complexity Analysis**

Here N is the number of nodes and E is the number of total edges in the given network.

- Time complexity: O((N−1)!+ElogE)
  
  In a complete graph with N nodes and N∗(N−1) directed edges, we can end up traversing all the paths of all the possible lengths. The total number of paths can be represented as ∑len=1N​(lenN​)∗len!, where `len` is the length of path which can be 1 to N. This number can be represented as e.N!, it's essentially equal to the [number of arrangements](https://oeis.org/wiki/Number_of_arrangements) for N elements. In our case, the first element will always be K, hence the number of arrangements is e.(N−1)!.
  
  Also, we sort the edges corresponding to each node, this can be expressed as ElogE because sorting each small bucket of outgoing edges is bounded by sorting all of them, using the inequality xlogx+ylogy≤(x+y)log(x+y). Also, finding the minimum time required in `signalReceivedAt` takes O(N).

- Space complexity: O(N+E)
  
  Building the adjacency list will take O(E) space and the run-time stack for DFS can have at most N active functions calls hence, O(N) space.

---

### Approach 2: Breadth-First Search (BFS)

**Intuition**

> If you're not familiar with BFS, check out our [Graph Explore Card](https://leetcode.com/explore/featured/card/graph/620/breadth-first-search-in-graph/).

Similar to the previous approach, we will simulate the signal and send it through the nodes as per the problem description but this time using BFS. Starting from node k, the signal will travel to the adjacent nodes along the directed edges. We will track the signal movement with respect to time in a Breadth-First Search manner.

We will initialize the queue with the node `currNode` as k and store the corresponding time required in `signalReceivedAt` as `0`. The signal from node `currNode` will travel to every adjacent node. Iterate over every adjacent node `neighborNode`. We will add each adjacent node to the queue only if the signal from `currNode` via the current edge takes less time than the fastest signal to reach the adjacent node so far. Time taken by the fastest signal for `currNode` is denoted by `signalReceivedAt[currNode]`.

**Algorithm**

1. Create an adjacency list such that `adj[source]` contains all destination nodes (`dest`) that the signal can travel to from the source node (`source`). For each destination node, there will be a pair `(time, dest)`. Here, `time` denotes the time required for the signal to travel from `source` to `dest`.

2. For all nodes, initialize `signalReceivedAt` as a large value to signify that, so far, no signal has been received.

3. Add k to the queue. While the queue is not empty:
   
   - Pop the front node `currNode` from the queue
   - Traverse all the edges connected to `currNode`. Add the adjacent node `neighborNode` to the queue only if the signal takes less time than the value at `signalReceivedAt[neighborNode]`. Update the time at `signalReceivedAt[neighborNode]` to current signal time.

4. Find the maximum value in the array `signalReceivedAt`. If any value in `signalReceivedAt` is still the large value we initialized the array with, then return -1 as that node is not reachable from `k`. Otherwise, return the maximum value in the array.

**Implementation**

class Solution {
public:
    // Adjacency list, defined it as per the maximum number of nodes
    // But can be defined with the input size as well
    vector<pair<int, int>> adj[101];

    void BFS(vector<int>& signalReceivedAt, int k) {
        queue<int> q;
        q.push(k);
    
        // Time for starting node is 0
        signalReceivedAt[k] = 0;
    
        while (!q.empty()) {
            int currNode = q.front(); 
            q.pop();
    
            // Broadcast the signal to adjacent nodes
            for (pair<int, int> edge : adj[currNode]) {
                int time = edge.first;
                int neighborNode = edge.second;
    
                int arrivalTime = signalReceivedAt[currNode] + time;
                if (signalReceivedAt[neighborNode] > arrivalTime) {
                    // Fastest signal time for neighborNode so far
                    // signalReceivedAt[currNode] + time : 
                    // time when signal reaches neighborNode
                    signalReceivedAt[neighborNode] = arrivalTime;
                    q.push(neighborNode);
                }
            }
        }
    }
    
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Build the adjacency list
        for (vector<int> time : times) {
            int source = time[0];
            int dest = time[1];
            int travelTime = time[2];
    
            adj[source].push_back({travelTime, dest});
        }
    
        vector<int> signalReceivedAt(n + 1, INT_MAX);
        BFS(signalReceivedAt, k);
    
        int answer = INT_MIN;
        for (int i = 1; i <= n; i++) {
            answer = max(answer, signalReceivedAt[i]);
        }
    
        // INT_MAX signifies atleat one node is unreachable
        return answer == INT_MAX ? -1 : answer;
    }

};

**Complexity Analysis**

Here N is the number of nodes and E is the number of total edges in the given network.

- Time complexity: O(N⋅E)
  
  Each of the N nodes can be added to the queue for all the edges connected to it, hence in a complete graph, the total number of operations would be O(NE). Also, finding the minimum time required in `signalReceivedAt` takes O(N).

- Space complexity: O(N⋅E)
  
  Building the adjacency list will take O(E) space and the queue for BFS will use O(N⋅E) space as there can be this much number of nodes in the queue.

---

### Approach 3: Dijkstra's Algorithm

**Intuition**

> If you're not familiar with Dijkstra's Algorithm, check out this topic in our [Graph Explore Card](https://leetcode.com/explore/featured/card/graph/622/single-source-shortest-path-algorithm/3862/).

As mentioned earlier, our objective is to find the fastest path from node k to every other node. This is a typical use case for the Single Source Shortest Path algorithm. Hence, In this approach, we will use Dijkstra's Algorithm to find the fastest path to every node from node k.

This approach is very similar to the previous BFS approach. We will start with node k and then iterate over every adjacent node `neighborNode`. In the previous approach, we used a queue and hence broadcasted the signal from visited nodes in a FIFO manner. However, in this approach, we will use a priority queue to traverse the nodes in increasing order of the time required to reach them. Therefore, in each iteration, we will visit the node with the shortest travel time. This will help us in finding the fastest time path first.

**Algorithm**

1. Create an adjacency list such that `adj[source]` contains all destination nodes (`dest`) that the signal can travel to from the source node (`source`). For each destination node, there will be a pair `(time, dest)`. Here, `time` denotes the time required for the signal to travel from `source` to `dest`.

2. For all nodes, initialize `signalReceivedAt` as a large value to signify that, so far, no signal has been received.

3. Initialize priority queue with the pair of starting node k and its distance 0, store its distance in `signalReceivedAt` as 0. While the priority queue is not empty:
   
   - Pop the top node `currNode` from the priority queue.
   - Traverse all outgoing edges connected to `currNode`.
   - Add the adjacent node `neighborNode` to the priority queue only if the current path takes less time than the value at `signalReceivedAt[neighborNode]`. Update the time at `signalReceivedAt[neighborNode]` to current path time.

4. Find the maximum value in the array `signalReceivedAt`. If any value in `signalReceivedAt` is still the large value we initialized the array with, then return -1 as that node is not reachable from `k`. Otherwise, return the maximum value in the array.

**Implementation**

class Solution {
public:
    // Adjacency list, defined it as per the maximum number of nodes
    // But can be defined with the input size as well
    vector<pair<int, int>> adj[101];

    void dijkstra(vector<int>& signalReceivedAt, int source, int n) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, 
        greater<pair<int, int>>> pq;
        pq.push({0, source});
    
        // Time for starting node is 0
        signalReceivedAt[source] = 0;
    
        while (!pq.empty()) {
            int currNodeTime = pq.top().first;
            int currNode = pq.top().second; 
            pq.pop();
    
            if (currNodeTime > signalReceivedAt[currNode]) {
                continue;
            }
    
            // Broadcast the signal to adjacent nodes
            for (pair<int, int> edge : adj[currNode]) {
                int time = edge.first;
                int neighborNode = edge.second;
    
                // Fastest signal time for neighborNode so far
                // signalReceivedAt[currNode] + time : 
                // time when signal reaches neighborNode
                if (signalReceivedAt[neighborNode] > currNodeTime + time) {
                    signalReceivedAt[neighborNode] = currNodeTime + time;
                    pq.push({signalReceivedAt[neighborNode], neighborNode});
                }
            }
        }
    }
    
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Build the adjacency list
        for (vector<int> time : times) {
            int source = time[0];
            int dest = time[1];
            int travelTime = time[2];
    
            adj[source].push_back({travelTime, dest});
        }
    
        vector<int> signalReceivedAt(n + 1, INT_MAX);
        dijkstra(signalReceivedAt, k, n);
    
        int answer = INT_MIN;
        for (int i = 1; i <= n; i++) {
            answer = max(answer, signalReceivedAt[i]);
        }
    
        // INT_MAX signifies atleat one node is unreachable
        return answer == INT_MAX ? -1 : answer;
    }

};

**Complexity Analysis**

Here N is the number of nodes and E is the number of total edges in the given network.

- Time complexity: O(N+ElogN)
  
  Dijkstra's Algorithm takes O(ElogN). Finding the minimum time required in `signalReceivedAt` takes O(N).
  
  The maximum number of vertices that could be added to the priority queue is E. Thus, push and pop operations on the priority queue take O(logE) time. The value of E can be at most N⋅(N−1). Therefore, O(logE) is equivalent to O(logN2) which in turn equivalent to O(2⋅logN). Hence, the time complexity for priority queue operations equals O(logN).
  
  Although the number of vertices in the priority queue could be equal to E, we will only visit each vertex only once. If we encounter a vertex for the second time, then `currNodeTime` will be greater than `signalReceivedAt[currNode]`, and we can continue to the next vertex in the priority queue. Hence, in total E edges will be traversed and for each edge, there could be one priority queue insertion operation.
  
  Hence, the time complexity is equal to O(N+ElogN).

- Space complexity: O(N+E)
  
  Building the adjacency list will take O(E) space. Dijkstra's algorithm takes O(E) space for priority queue because each vertex could be added to the priority queue N−1 time which makes it N∗(N−1) and O(N2) is equivalent to O(E). `signalReceivedAt` takes O(N) space.
