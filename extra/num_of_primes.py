

# find number of prime number till n

# this works but it is bad implementation.

# there is no need for isPrime function, any composite number will
# automatically be turned by the smaller prime numbers.

# Hindsight: sieve will catch the composites no matter what because composite
# numbers are made of smaller prime numbers, they can't get overlooked.

'''
The Sieve of Eratosthenes: 
An efficient algorithm that can be used to count the number of prime numbers up to n.

e.g. n=100
create a list of size n ALL with value True.
run a loop starting from 2 (first prime number) until n**(1/2)
mark all multiples of list elements from 2 to n**(1/2) as false.
by the end, only True elements in the list will be prime numbers.

'''

def sieve(n):
    primes = [True]* (n+1) # n+1 because index 0 to n is n+1 elements
    composites = n-1
    a = 2 # first prime
    while a*a <= n: # same as saying a <n**(1/2)
        if primes[a]: # if true, it is prime and all its multiples should be marked false.

            for i in range(a*a,n+1,a):
                primes[i] = False    
        a+=1
                
    return len([x for x in primes[2:] if x]) # starting from index 2, because index 0,1 are are True and do not count as primes
  
print(f"the number of primes upto 100 is: {sieve(100)}")
n = 1
while n!= -1:
    print("\n Try another number")
    n = int(input("Enter n: "))
    print(f"the number of primes till {n} is {sieve(n)}")

        





