# Algorithm to figure out if a given number is perfect number or not.
# A perfect number is a positive integer equal to the sum of its proper divisors excluding itself.
# e.g 6 = 1+2+3 and 28 = 1+ 2 +4 + 7 + 14


# solution plan: find and append all proper divisors of the given +ive integer to an array, get thier sum
# if sum is equal to the number, we found perfect number, otherwise not.


def getSumOfAllDivs(n):
    divs = [1]
    sum1 = 1
    temp = 2 # start search from 2
    while n/temp not in divs:
        candidate = n/temp # e.g. 12/2, if we get integer and not decimal. we will append temp and n/temp to the list
        
        if candidate == int(candidate): # checking if candidate divisor is integer (and not a decimal)
            if candidate != temp:
                divs.append(int(candidate))
                sum1+=candidate
            divs.append(int(temp))
            sum1+=temp
            
        temp+=1
    
    divs.sort()
    
    return divs,sum1
            
        
        
n = 0
while n!= -1: # testing stops if user enters -1
    n = int(input())
    divArray,sumDivs = getSumOfAllDivs(n)
    output = f"{n} is NOT perfect.   "
    if n == sumDivs:
        output = f'{n} = '
        for i in divArray:
            output+= f'{i} + '
    print(output[:-3])
    print(divArray)
    