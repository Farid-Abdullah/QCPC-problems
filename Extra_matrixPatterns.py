



#Problem explantion:
'''
The first line of the input is number of columns for a matrix.
followed by matrix aand,the items of the matrix contain either 0 or 1
example input:
5
1 1 0 0 1
0 0 1 1 0
0 0 0 0 0

all input is in the string format.

The task:
Given that:
   L = 1 0 0   and  0 0 1 and 1 1 1  and 1 1 1
       1 0 0        0 0 1     1 0 0      0 0 1
       1 1 1        1 1 1     1 0 0      0 0 1

and N = 1 0 1  and 1 1 1
        1 1 1      0 1 0
        1 0 1      1 1 1

and U = 1 0 1  and 1 1 1  and 1 1 1 and 1 1 1
        1 0 1      1 0 1      1 0 0     0 0 1
        1 1 1      1 0 1      1 1 1     1 1 1
We have process/iterate over the given matrix and find all possible instances of L, N and U return their count.

example X
1 1 1 0 1
0 0 1 0 1
0 0 1 1 1
1 1 1 0 1
In the above matrix, L = 2, N = 1 and U = 1 ( I think)

'''

# concept solution
'''
1.  we can hardcode the different matrices into L,N and U varaibles
    like L = ['100100111','001001111,'111100100','111001001']
    or instead of binary as string, we can replace it by numbers that represented by those binary
    like the above L will become: L = [295, 79, 484,457]
    do the same thing for the N and U
2. We need a way to iterate over all the possible submatrices of 3 rows and 3 column,
    first i will try to put all the input of the matrix into a single string,
    e.g. example X on line 32 will become: '11101001010011111101'
    then, loop over the range using while loop,
    

'''




columns = int(input("number of columns:"))
x = ''
while True:
    try:
        line = input("")
        x+= line
        assert line!= ''
    except:
        break




def method_1():
    '''
    L,M and U will be set of numbers
    '''
    global x
    global columns
    x = x.replace(' ','')
    x = x.replace('\n','')


    res = ''
    temp =0
    row_count = 1


    L = {295, 79, 484,457}
    N = {381,471}
    U = {367,493,487,463}
    count_L = 0
    count_N = 0
    count_U = 0
    i = 0
    while i< len(x):
        if i!=0 and i+2 == columns*row_count:
            i +=2 # goes to next row if i is at second last column
            row_count+=1
            
        
       
        #following 6 lines are for creating the submatrix, but in string format
        res+= x[i+temp*columns:i+temp*columns+3]
        temp+=1
        res+= x[i+temp*columns:i+temp*columns+3]
        temp+=1
        res+= x[i+temp*columns:i+temp*columns+3]
        temp=0

        
        
        

            
        
        if len(res) != 9: # this would mean i is at second last row, no further possible sub matrices
            break
            
        num = int(res,2)
        if num in L:
            count_L+=1
            
        elif num in N:
            count_N+=1
        elif num in U:
            count_U+=1
        
        res = ''
        i+=1
    print("count of L: ", count_L)
    print("count of N: ",count_N)
    print("count of U: ",count_U) 

def method_2():
    '''
    L,N and U will be set of binary strings
    '''
    global x
    global columns
    x = x.replace(' ','')
    x = x.replace('\n','')


    res = ''
    temp =0
    row_count = 1


    L = {'111100100', '100100111', '111001001', '001001111'}
    N = {'101111101', '111010111'}
    U = {'101101111', '111101101', '111001111', '111100111'}
    count_L = 0
    count_N = 0
    count_U = 0
    i = 0
    while i< len(x):
        if i!=0 and i+2 == columns*row_count:
            i +=2 # goes to next row if i is at second last column
            row_count+=1
            
        
       
        #following 6 lines are for creating the submatrix, but in string format
        res+= x[i+temp*columns:i+temp*columns+3]
        temp+=1
        res+= x[i+temp*columns:i+temp*columns+3]
        temp+=1
        res+= x[i+temp*columns:i+temp*columns+3]
        temp=0

        
        
        

            
        
        if len(res) != 9: # this would mean i is at second last row, no further possible sub matrices
            break
            
        
        if res in L:
            count_L+=1
            
        elif res in N:
            count_N+=1
        elif res in U:
            count_U+=1
        
        res = ''
        i+=1
    print("count of L: ", count_L)
    print("count of N: ",count_N)
    print("count of U: ",count_U) 



print("Method 1, where L, N , U are set of numbers: ")
method_1()
print("Method 2, where L, N, U are set of binary strings")
method_2()








