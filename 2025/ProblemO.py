

'''
testcases:
3
3 3
5 4 1
6 2
3 2 0 4 5 10
1 2
5
'''

t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    arr = [int(x) for x in input().split()]
    
    