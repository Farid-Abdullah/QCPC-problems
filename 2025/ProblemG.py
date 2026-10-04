

s = set()
q = int(input())
for _ in range(q):
    t,x = map(int, input().split())
    if t == 1:
        s.add(x)
        