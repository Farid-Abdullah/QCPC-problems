


def findMin(m, start, last):
    pass
    
tests = int(input(""))
for test in range(tests):
    array = input("").split(" ")
    array = [int(x) for x in array]

    q = int(input())

    for query in range(q):
        lr = input().split(" ")
        l,r = int(lr[0])-1,int(lr[1])
        array_lr = array[l:r]
        theMin = min(array_lr)
        sub_arrays = []
        count = 0
        for i in range(len(array_lr)):
            for j in range(i+1, len(array_lr)+1):
                first = array_lr[i:j]
                second = array_lr[0:i] +array_lr[j:len(array_lr)]
                print(first, second)
                if first == [] or second == []:
                    continue
                if min(first) == min(second):
                    count+=1
        print(count)

def method2():
    ''' Uses findMin function and doesn't require an additional subarray'''
    tests = int(input(""))
    for test in range(tests):
        array = input("").split(" ")
        array = [int(x) for x in array]

        q = int(input())

        for query in range(q):
            lr = input().split(" ")
            l,r = int(lr[0])-1,int(lr[1])
            array_lr = array[l:r]
            theMin = min(array_lr)
            
            count = 0
            for i in range(len(array_lr)):
                for j in range(i+1, len(array_lr)+1):
                    print(first, second)
                    if first == [] or second == []:
                        continue
                    if findMin( == min(second):
                        count+=1
            print(count)
            
             
                    
                
        
