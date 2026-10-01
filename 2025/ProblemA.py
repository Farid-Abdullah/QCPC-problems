
# Although I tried to optimize the solution,
# This is still a brute force solution. Not efficient at all and will certainly get TLE due to O(Q *K^3)
# where Q is number of queries and K is the average size of the subarray for each query (worse case k = n = 100000)
# 

def findMin(m, arr,start, last):
    first = False
    second = False
    i = 0
  
    while i<len(arr) and not( first and second):
        if not first and start<=i<last and m == arr[i]:
            first = True
        elif not second and (i<start or i>=last) and m==arr[i]:
            second = True
        i+=1
    return first and second
    
def method2():
    ''' Uses findMin function and doesn't require an additional subarray'''
    # hardcoding test cases for simplicity:
    n = 8
    #array = input("").split(" ")
    #array = [int(x) for x in array]
    array = [5,2,3,2,2,3,2,5]

    q = 5

    for query in range(q):
        lr = input().split(" ")
        l,r = int(lr[0])-1,int(lr[1])
        array_lr = array[l:r]
        theMin = min(array_lr)
        
        count = 0
        for i in range(len(array_lr)):
            for j in range(i+1, len(array_lr)+1):
                if findMin(theMin,array_lr,i,j):
                    count+=1
        print(count)

method2()
             
                    
                
        
