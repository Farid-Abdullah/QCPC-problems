# first time using DFS

# problem find the number of islands:
'''
given a 2x2 matrix, all horizontally and vertically connected 1s are part of an
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
    ["1","1","1"],
    ["0","0","1"],
    ["1","1","1"]
]
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





















    
