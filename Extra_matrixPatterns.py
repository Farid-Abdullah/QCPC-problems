



#Problem explantion:
'''
The first line is indicate the number of cases.
The second line of the input is number of rows for a matrix.
followed by matrix aand,the items of the matrix contain either 0 or 1
example input:
3
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
    then, loop over the range using while loop.

3. the first submatrix from X (line 33) has an L, if I had to locate it in the now string format from line 51
    it would be: "[111]01[001]01[001]...." The index of the submatrix's on the X goes like: 0,1,2,  5,6,7,  10,11,12
    I see a pattern here, if i loop over X, for every iteration, I will create a nested loop that runs three times
    like: for temp in range(3): X[i+temp*columns:i+temp*columns+3], let's say i = 0, the three
    iterations will be: X[0:3], X[5:8], X[10:13] which gives the indices needed for the first submatrix (line 55)
    let's go over one more submatrix, the last one in X, which has N in it and its X indices are: 7,8,9,  12,13,14  17,18,19
    in the loop: for temp in range(3): X[i+temp*columns:i+temp*columns+3], if i = 7
    the iterations will be: X[7:10], X[12:15], X[17:20], which is what we need for the last matrix.
    
4. just run "if submatrix in L:" same for N and U with suitable counters and the rest is straightforward.
    
    
Note: I am reading the inputs from an external file '06.txt' which has 6 test cases and i am applying algorithm on them
Note 2: I created two functions for the same algorithm, method_1 and method_2
        , one where the hardcoded values of L,M and U are sets of binary strings, one where
        hardcoded values are numbers corresponding to its binary strings. the plan was to test the performance of both.
'''









def method_1(x,columns):
    '''
    x is the matrix in string format, columns is the number of columns in it
    Here L,N and U will be set of numbers
    '''
    
    
   


    res = ''
   
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
        for temp in range(3):
            res+= x[i+temp*columns:i+temp*columns+3]
      

        
        
        

            
        
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

def method_2(x,columns):
    '''
    x is the matrix in string format, columns is the number of columns in it
    Here L,N and U will be set of binary strings
    '''
   


    res = ''
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
            
        
       
        #The loop for creating a submatrix from the string X
        for temp in range(3):
            res+= x[i+temp*columns:i+temp*columns+3]
        

        
        
        

            
        
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





with open("06.txt", "r") as file_object:
        line_lists = file_object.readlines()
        for i in range(len(line_lists)):
            line_lists[i] = line_lists[i].replace(" ","")
            line_lists[i] = line_lists[i].replace("\n","")
            


test_cases = line_lists[0]
j = 0
line_index = 0
print(test_cases)
while j<int(test_cases):
    
    if line_index>=len(line_lists):
            break
    
    rows = int(line_lists[line_index+1])
    print(rows)

    columns = len(line_lists[line_index+2])
    
    x = ''
    line_index+=1
    for i in range(rows):
        line_index+=1
        if line_index>=len(line_lists):
            break
        print(line_lists[line_index])
        x+= line_lists[line_index]

    
    
    j+=1
    #method_1(x,columns)
    method_2(x,columns) 
    






