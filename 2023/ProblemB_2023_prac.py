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

    def split_and_count(arr, mVal, mi,offset=0): # Need for offset variable is that we won't need a loop to decrement the subarray !! saving big chunk on time complexity!!!
        decBy = mVal+base-offset 
        state["answer"]+= decBy
        sub1 = arr[mi+1:]

        if sub1 != []:
            mVal1= min(sub1)
            mi1= sub1.index(mVal1)
            split_and_count(arr[mi+1:],mVal1, mi1,decBy+offset)
    
        sub2 = arr[:mi]
        if sub2 !=[]:
            mVal2= min(sub2)
            mi2= sub2.index(mVal2)
            split_and_count(arr[:mi],mVal2, mi2,decBy+offset)

    split_and_count(arr, mVal, mi)
    print(state["answer"])


sol1()