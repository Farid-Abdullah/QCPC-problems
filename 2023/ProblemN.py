# Problem N. No Adjacent Sum
# The first line of the input indicate the number of test cases t, 
# for every test case there is a single line containing three integers a,b and k
# constraints for t,a,b and k: 0<t<1001  0<a<b<10^18   -1<k<28
# Output: the number of integers between a and b (inclusive) that do not have three
#         adjacent digits whose sum is equal to k.

'''
solution algorithm:
a number that we can get from the sum of three consecutive numbers is always
divisible by 3, example 012 = 3  123 =6 234 = 9 and so on

1. since k is always less than 28, the first condition will check whether
    k is divisible by 3. if not, then just return b-a+1.

2. in the test case of the three consecutive integers, the middle integer times three
    is equal to there sum, e.g. 0+1+2 = 3 == 1*3,  1+2+3 == 2*3, 5+6+7 == 6*3 and 8+9+10 == 9*3
3. We can figure out which middle integer is it that we are looking for, by doing k/3,
    which for 27 will give us 9, for 24 it will give us 8
4. Now we just need to ensure a<k/3<b, if this condition is true, we return (b-a+1)-3

The a<(k/3)<b is the only condition i need to check.


'''

def NoAdjacentSum(t):
    for i in range(t):
        integerLine = input("") # this will take the three integers separated by space "a b k"
        a,b,k = integerLine.split(' ')# [a,b,k]
        a,b,k = int(a),int(b),int(k) 
        answer = b-a+1 # answer if three integers aren't there
        if a<(k/3)<b:
            print(answer-3)
        else:
            print(answer)


testCases = int(input(":")) # for inputing test cases
NoAdjacentSum(testCases)
        
        
