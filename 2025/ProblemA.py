
# a much better approach than previous one which was something like O(n^3) in worse case.
# This one uses two pointer approach with compleity O(n2) in worst case (because num of queries == n == 10^5)
n = int(input()) # input size of array
arr = list(map(int, input().split()))

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -=1
    r -=1
    p1,p2 = l,r
    candMin = float('inf')
    foundBoundary = False
    theMin = min(arr[p1:p2+1])
    sol = 0
    while p1 < p2: # two pointer approach
        #find first and last occurence of minimum in the range.
        if arr[p1] != theMin:
            p1 += 1
        elif arr[p2] != theMin:
            p2 -= 1
        else:
            foundBoundary = True
            break
    if foundBoundary:
        diff = p2 - p1
        sol = diff*(p1+1-l) + diff*(r-p2+1)
        #linear search for the remaining minimuns in the p1 to p2 range.
        i = p1+1
        while i < p2:
            if arr[i] == theMin:
                sol += (i-p1)* (p2-i)
                p1 = i
            i += 1
    print(sol)




            




        
        