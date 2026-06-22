

# find number of prime number till n

# this works but it is bad implementation.

# there is no need for isPrime function, any composite number will
# automatically be turned by the smaller prime numbers.

# Hindsight: sieve will catch the composites no matter what because composite
# numbers are made of smaller prime numbers, they can't get overlooked.

def isPrime(num):
    for i in range(2, num):
        if num%i == 0:
            
            return False
    
    return True
    

def sieve(n):
    root_n = round(n**(1/2))
    count = 0
    grid = [0]*n

    for i in range(2,root_n+1):
        if isPrime(i):
            temp = 2*i -1
            while temp < n:
                grid[temp] = 1
                temp+= i
                
                count+=1
                
                
    print("total primes: ", grid.count(0) - 1)

n = int(input("enter n: "))
sieve(n)



