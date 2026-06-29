# Problem B: Begins and it  || 
# goal: 
# given an array, you can increment all elements by 1 or decrement all elements in the its subarray.
# return minimum number of operations that will make all elements equal to 0

# test cases:
'''
1.
    input:
    5
    -2 0 5 7 1
    output: 11
2.
    input:
    10
    0 1 0 2 0 3 0 4 0 5
    output: 15
3.
    input: 
    11
    -5 0 4 6 3 8 2 1 0 9 0
    ouput: 30
'''
def sol1():
    '''
    Could be improved, for example, the loop in line 47, that loop could make the time complexity O(n2), I think we can avoid the loop using offset variable.
    '''
# hardcoding case 3:
    n = 11 # 
    arr = [-5, 0, 4, 6, 3, 8, 2, 1, 0, 9]
    #arr = [0,1,0,2,0,3,0,4,0,5]
    state = {"answer":0}

    mVal = min(arr)
    mi = arr.index(mVal)

    if mVal<0:
        base = abs(mVal)
        state["answer"] =base # counting the max number of increments that will happen on the entire array.
    else:
        base = 0

    def split_and_count(arr, mVal, mi):
        decBy = mVal+base
        state["answer"]+= decBy
        
        for i in range(len(arr)):
            arr[i]-=decBy
            

        sub1 = arr[mi+1:]
        if sub1 != []:
            mVal1= min(sub1)
            mi1= sub1.index(mVal1)
            split_and_count(arr[mi+1:],mVal1, mi1)
    
        sub2 = arr[:mi]
        if sub2 !=[]:
            mVal2= min(sub2)
            mi2= sub2.index(mVal2)
            split_and_count(arr[:mi],mVal2, mi2)

    split_and_count(arr, mVal, mi)
    print(state["answer"])


sol1()