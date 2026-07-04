# important lesson: How to perform AND, OR and XOR operations on int base 2.
# bitwise operations: AND = &, OR = |, XOR = ^


# Problem C. Can look like a
'''
Given a number x, return min number of beutiful numbers that can XOR to get x, or indicate it is impossible
a number is beutiful if its first and last bit is 1 and all middle ones are 0. e.g. 3(11), 5(101) and 9(1001) are beutiful.
'''
# test cases:

'''
input: 
5 # number of test cases
3
15
9
4
85931740

outpu: 
1 
3 
1 
-1 
16
'''


'''
There are a few patterns that i get when i XOR beautiful numbers.
1. XORing odd number of beutiful binary numbers will result in an odd number, e.g. we get 15 by XORing 11(3),101(5),1001(9), and XORing even number of beautiful bin numbers will result in an even number
2. Instead of XORing beutiful binary numbers, i can just add multiples of 2 to reach x. for example I get 15 by adding 8,4,2,1(2power0) which means i used 4-1 multiples of 2
2. I can get 15 by adding 1000,100,10,1 (the final 1 is additional because 15 is odd) which are 8+4+2+1 = 15, therefore i used 4-1 (-1 because 15 was odd) beautiful numnbers to get 15
3. I can get 18 by adding 10000,10 which are 16+2, therefore i used 2 beautiful numbers to get 18
4. I cannot get 13 by adding beautiful numbers, but the process to find that out will be to add 1000(8),100(4) ,1(additional one for odd) which would mean that 13 probably required xoring 3-1 beautiful numbers,
   But according to my point 1, that is not possible, Xoring 2 beautiful numbers cannot get me an odd number, that's why i return -1 for 13
5. Point 4 applies to even numbers like 14 but in the opposite way, like xoring odd number of beautiful numbers will never get me 14, therefore i must return -1
'''


t = int(input()) # no of test cases
for _ in range(t):
    x = int(input())
    count = 0
    while x >1:
        temp = x.bit_length()-1
        sub = int("1"+"0"*temp,2)
        x = x-sub
        count+=1
    if x==1 and count%2==0 or x==0 and count%2==1:
        print(-1)
    else:
        print(count)
