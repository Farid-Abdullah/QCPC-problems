

# Problem M: Abdo With Array

'''
problem explanation:
inputs:  T for number of test cases
         N and X for first line of every test case, N is length of array, X is desired 
         array 'A' for second line of every test case
what to do:
            In case Ai>=1 We are allowed this operation: Ai = Ai -1 where
            A is the array and i is any index in A.
            We have to apply the minimum number of operations to indices of A
            such that A goes in a state where the sume of adjacent numbers is less or equal to X
            e.g. N = 3, X = 3 , A = [2,2,2], then we can decrement A[1] making A = [2,1,2]
            now all adjacent element of A give sum equal to 3 which is A[0]+A[1] and A[1]+A[2] = 2+1 and 1+2
output:
        Output the minimum number of operations required to take the array into the required state
'''
# solution:
'''
first of all i will have a decrement tracker that will track all the decrements I did, and then display it by the end
1. I will check if A[0]>X, if yes I will decrement it till its false. (while loop)
2. Next I will check if A[0]+A[1] <= X if not, keep decrementing A[1] (while loop)
3. I will apply step 2 on all elements till i reach last, so outer for loop that goes till N-1
4. then i will output decrement_tracker
'''

T = int(input("")) # test cases

for test_case in range(T):
    dec_counter = 0
    N,X = input("").split(' ')
    N,X = int(N), int(X)
    A = input("").split(' ')
    A = [int(x) for x in A]
    for adj in range(N-1):
        while A[adj] > X:
            A[adj]-= 1
            dec_counter +=1
        while A[adj]+ A[adj+1] >X:
            A[adj+1]-=1
            dec_counter+=1
    print(dec_counter)
        
            
            


