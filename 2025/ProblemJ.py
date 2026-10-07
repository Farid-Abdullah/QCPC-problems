

t = int(input())

# only possible combinations whose every sum of non-empty contigious subarray will be prime:
possible = [[2,3],[2],[3],[3,2],[2,3,2],[2,2,3],[3,2,2]]

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    if a in possible:
        if len(a)==3:
            print("2 3 2")
        elif len(a)==2:
            print("2 3")
        else:
            print(a[0])
    else:
        print("-1")
