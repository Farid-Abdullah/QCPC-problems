# first time using DFS

# problem find the number of islands:
'''
given a nxm matrix, all horizontally and vertically connected 1s are part of an
island, and 0s represent water. count number of islands.

e.g.
input:
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

Output: 1

Input:
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Output: 3


m = [
    ["1","1","1"],
    ["0","0","1"],
    ["1","1","1"]
]
ouput: 1
'''

# node = (x,y) where x and are y are indices of the 2d matrix


m = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# Bad implementation of DFS, but works. I will try to improve it later. 

# Gemini comments:
'''
# Issues with this Recursive Set-Based DFS:

1. Stack Overflow (Recursion Limit): The recursion depth equals the size of the island. 
   On a connected island or snake-like grid of size O(N * M), the call stack grows linearly O(N), 
   triggering a RecursionError on large inputs (e.g., 100x100 grid of all "1"s = 10,000 frames deep).

2. Unnecessary O(N * M) Memory Overhead: Maintaining a separate `visited = set()` 
   allocates extra memory and incurs hash-computation overhead for every coordinate tuple (x, y).

3. Redundant Visited Tracking: Since the grid matrix `m` is mutable, "sinking" the island 
   in-place by setting `m[x][y] = "0"` when visited completely eliminates the need for a separate 
   `visited` set.

4. Global Variable Dependence: Relying on global variables (`visited`, `height`, `width`) 
   makes the code prone to state bugs and harder to wrap cleanly into a class or function 
   for modular testing.

Solution: Use an iterative DFS with an explicit `stack` list (or iterative BFS with `deque`) 
and sink visited land in-place (`m[x][y] = "0"`). This guarantees O(1) call-stack depth, 
prevents stack overflow, and optimizes space complexity.
'''


visited = set()
count = 0
height = len(m)
width = len(m[0])
def dfs(x,y):

    if x>= height or y>= width:
        return
    if x<0 or y<0:
        return
    if m[x][y] == "0":
        return
    if (x,y) in visited:
        return
    visited.add((x,y))
    #print(visited)
    
    # going right:
    dfs(x,y+1)
    #going down
    dfs(x+1, y)
    # going left:
    dfs(x, y-1)
    # going up:
    dfs(x-1, y)
    
    

for x in range(height):
    for y in range(width):
        if m[x][y] == "1" and (x,y) not in visited:
            dfs(x,y)
            count+=1
print(count)





















    
