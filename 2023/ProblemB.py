


def AD(n,m):
    ''' takes two integerr, creates a nxm matrix where the difference of adjacent numbers is either 1 or even number'''
    matrix = []
    matrix2 = []
    temp = 0
    temp2 = 0
    
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append((temp+1))
            temp+=1
            
        
        temp2+=1
        
    
    if n%2 ==0 and m%2 ==0:
        return matrix
    elif n%2 == 1 and m%2 ==1:
        for i in range(m-1):# take care of last column
            matrix[i+1][m-1] = matrix[1][i]
        temp = matrix[n-1][m-1]+1
        for j in range(n-1,0,-1):
            for i in range(m-2,-1,-1):
                matrix[j][i] = temp
                temp+=1
        return matrix
    elif n%2 == 1:
        return matrix
    else:
        temp = 1
        for i in range(m):
            for j in range(n):
                matrix[j][i] = temp
                temp+=1
        return matrix

print('2x2 :',AD(2,2))
print('2x3 :', AD(2,3))
print('3x4 :', AD(3,4))
print('5x5 :',AD(5,5))


    


    
