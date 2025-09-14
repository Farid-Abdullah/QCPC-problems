

#Problem L Second Best Gain

'''
problem explanation: given a list "array" of length n, extract a subarray 'subArray' from it such that (n-len(subArray))*max2
is the largest you can get.
e.g. if n = 5 and array = [1,2,3,4,5]  if we extract subArray = [4,5] then applying the formula we get 12.

'''
#solution:
'''

I will make all possible subArrays from array, store them in a set, and then apply the formula to each one
and catch the largest number produced.

I am not sure what happens if the size of the array is too big, like 10^5, because then the set containing the subarrays
will become very large and I don't know if that's optimal at all
'''



n = int(input(''))

arrayString = input('').split(' ')
array = [int(x) for x in arrayString]
subArrays = set()
for i in range(n+1):
    for j in range(2,n+1):
        tempArray = tuple(array[i:j])
        subArrays.add(tempArray)
m = 0
for i in subArrays:
    length = len(i)
    if length<2:
        continue
    maxi = max(i) # I have to remove this value from the list
    while maxi in i: # in case there are several instances of the same max value
        i = list(i)
        i.pop(i.index(maxi))
        i = tuple(i)
    max2 = max(i) # now max(i) will give me the second largest value.
    temp = (n-length)*max2
    if temp>m:
        m = temp
print(m)
