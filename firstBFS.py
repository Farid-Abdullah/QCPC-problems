

# first breadth first search algorithm:

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

m = [
     [2, 1, 1],
     [1, 1, 0],
     [0, 1, 1]
     ]
visited = set()
queue = set()
height = len(m)
width = len(m[0])
total_oranges = 0
minutes = 0
directions = [
    (1, 0),   # down
    (-1, 0),  # up
    (0, 1),   # right
    (0, -1),  # left
]

def visitAllDir(x,y):
    new_q = set()
    for dx, dy in directions:
        x2 = x+dx
        y2 = y+dy
        
        if 0<=x2<height and 0<=y2<width:
            print(x2, y2)
            if m[x2][y2] == 1:
                m[x2][y2] = 2
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
    minutes+=1
    bfs(new_q)
        
        
        
        
    

for x in range(len(m)):
    for y in range(len(m[x])):
        if m[x][y] == 2 or m[x][y] == 1:
            total_oranges+=1

    for y in range(len(m)):
        if m[x][y] == 2:
            queue = {(x,y)}
            bfs(queue)
            
























