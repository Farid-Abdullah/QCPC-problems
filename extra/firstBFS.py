

# first breadth first search algorithm implementation:

'''
Rotting Oranges

You are given an m x n grid where:

0 = empty cell
1 = fresh orange
2 = rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.

If it's impossible for all oranges to become rotten, return -1

Example 1
2 1 1
1 1 0
0 1 1

Minute 0:

2 1 1
1 1 0
0 1 1

Minute 1:

2 2 1
2 1 0
0 1 1

Minute 2:

2 2 2
2 2 0
0 1 1

Minute 3:

2 2 2
2 2 0
0 2 1

Minute 4:

2 2 2
2 2 0
0 2 2

Output:

4
Example 2
2 1 1
0 1 1
1 0 1

The bottom-left orange can never be reached.

Output:

-1
'''
import sys
sys.setrecursionlimit(5000) # 5000 here, but will depend on the input size of matrix
# Issues:
''' 
# Issues with this Recursive Set-Based BFS (After double checking the code with gemini):

1. Stack Overflow: Works for test case 7 only because sys.setrecursionlimit was increased. 
   When recursion depth scales linearly O(N) with input size, recursion causes 
   RecursionError or OS-level stack overflows on large grids. recursion is best for divide and conquer problems.

2. Unordered Queue Structure: Python `set` is unordered. BFS requires FIFO (First-In, 
   First-Out) ordering. While level-by-level batching avoided bugs here, `set` is conceptually 
   incorrect for general BFS queues.

3. High Memory Allocation & Hash Overhead: `new_q.union(...)` and `new_q.add()` allocate 
   multiple new set objects and compute hash values repeatedly on every single level. 

4. Redundant Memory & Tracking: Maintaining a `visited` set uses O(N) extra space. 
   Mutating `m[x2][y2] = 2` directly is enough to mark a cell as visited.

Solution: Use an iterative loop with `collections.deque` (or two lists for level-by-level tracking)
to achieve O(1) queue operations, safe call stack execution, and O(1) auxiliary space.

    '''


all_testcases = [
    # 1. Simple valid propagation (your code overcounts time here -> outputs 3 instead of 2)
    ([[2, 1, 1]], 2),
    
    # 2. No fresh oranges at all (only empty cells)
    ([[0]], 0),
    
    # 3. Only a single rotten orange initially
    ([[2]], 0),
    
    # 4. Fresh orange that can never be reached
    ([[1]], -1),
    
    # 5. Impossible to reach bottom-left orange (Example 2)
    ([[2, 1, 1], 
      [0, 1, 1], 
      [1, 0, 1]], -1),
    # 6. reachable with diff location of rotten orange
      ([
     [2, 1, 1,1,2],
     [1, 1, 0],
     [0, 1, 1,2]],2),
    
    # 7. Large line of oranges (triggers RecursionError in recursive BFS)
    ([[2] + [1] * 1000], 1000),
]

for i,(m,expected) in enumerate(all_testcases):

    visited = set()
    queue = set()
    height = len(m)
    width = len(m[0])
    oranges = {"total": 0, "rotten": 0}
    minutes = 0
    directions = [
        (1, 0),   # down
        (-1, 0),  # up
        (0, 1),   # right
        (0, -1),  # left
    ]
    answer = minutes
    def visitAllDir(x,y):
        new_q = set()
        for dx, dy in directions:
            x2 = x+dx
            y2 = y+dy
            
            if 0<=x2<height and 0<=y2<len(m[x2]) and (x2,y2) not in visited:
                
                if m[x2][y2] == 1:
                    m[x2][y2] = 2
                    oranges["rotten"] += 1
                    new_q.add((x2,y2))
        
        return new_q

                    
                    
        
    def bfs(q):
        global minutes
        if q == set():
            return
        new_q = set()
        for node in q:
            visited.add(node)
            new_q = new_q.union(visitAllDir(node[0],node[1]))
        bfs(new_q) 
        if new_q != set():
            minutes+=1
            
    for x in range(len(m)):
        for y in range(len(m[x])):
            if m[x][y] != 0:
                oranges["total"] += 1
            if m[x][y] == 2 and (x,y) not in visited:
                oranges["rotten"] += 1
                queue.add((x,y))
    bfs(queue)
    if oranges["total"] != oranges["rotten"]: # to see if all oranges are rotten by this point
        answer = -1
    else:
        answer = minutes # -1 because the last minute is counted even if no new oranges are rotten
    assert(answer == expected), f"Test case {i+1} failed: expected {expected}, got {answer}"

print("All test cases passed!")



















