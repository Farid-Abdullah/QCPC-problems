


# Problem: given nxm, fillout matrix with numbers from 1 to nxm, in a pattern where
# the difference of the adjacent sides will give you 1 or any even number
# e.g. if n = 2, m=2
# matrix = 1 2
#          3 4  (1 is adjacent to 2 and 3, with diffrence of 1 and even number, 4 is adjacent to 3 and 2 and vice versa.
'''
Solution algorith explanation:
senario 1: if n and m are both even, just write all the numbers in sequence in the matrix
example when n = 2, m = 4:
1 2 3 4
5 6 7 8

senario 2: if n is odd and m is even, the same thing as above
example n = 3, m = 2
1 2
3 4
5 6

senario 3: if n is even and m is odd, transpose of mxn
example n = 2, m = 3
mxn = 1 2
      3 4
      5 6
to
nxm = 1 3 5
      2 4 6

senario 4: if both are odd (this is the difficult part):
e.g n = 5, m = 5

step 1: fill the first row: matrix =   1 2 3 4 5

step 2: fill the last column while following the sequence of numbers:

matrix = 1 2 3 4 5
                 6
                 7
                 8
                 9
step 3: continue the sequence from bottom, fill up the empty spaces in reverse order:
i) matrix = 1  2  3  4 5
                       6
                       7
                       8
           13 12 11 10 9

The second last row:
ii) matrix =  1  2  3  4 5
                         6
                         7
             17 16 15 14 8
             13 12 11 10 9

and same for the remain rows:
iii) matrix = 1  2  3  4 5
             25 24 23 22 6
             21 20 19 18 7
             17 16 15 14 8
             13 12 11 10 
'''    # i realize the solution for odd n and odd m is wrong, in the above example 18 - 7 do not give me 1 or even number



def AD(n,m):
    ''' takes two integerr, creates a nxm matrix where the difference of adjacent numbers is either 1 or even number'''
    matrix = []
    temp = 1
    if m%2 == 0 or (m%2 == 1 and n%2 == 1): #taking care of senario 1 and 2 and setting stage for senario 4.
        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(temp)
                temp+=1
    else:  # only for senario 3
        for i in range(n):
            matrix.append([])
        for i in range(m):
            for j in range(n):
                matrix[j].append(temp)
                temp+=1
        return matrix
    
    if m%2 ==0: 
        return matrix # senario 1 2 and 3 taken care off by this point
    
    else: # senario 4 when n and m are both odd, the matrix is already filled with numbers
        # first row remains the same
        temp = matrix[0][m-1] +1
        for i in range(1,n): # loop for taking care of the last column
            matrix[i][m-1] = temp
            temp+=1
        for j in range(n-1,0,-1):
            for i in range(m-2,-1,-1):
                matrix[j][i] = temp
                temp+=1
        
            
        
        return matrix
        
    
print("Some test cases: ")
print('2x2 :',AD(2,2))
print('2x3 :', AD(2,3))
print('3x4 :', AD(3,4))
print('5x5 :',AD(5,5))
print('11x5 :', AD(11,5))
print('5x3 :', AD(5,3))


    


    
