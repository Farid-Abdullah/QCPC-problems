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



x = int("101",2)^int("10001",2)^int("100001",2)^int("10000001",2)^int("10000000001",2) # 1205 required XORing 5 beautiful numbers

x = 15
# I will keep subtracting biggest possible multiple of 2, until i reach 1 in case of odd x, 0 in case of even x,
# but now i have 1205 as my x, which should reach 1 after i subtract multiples of 2 five times.
# 1
temp = x.bit_length()-1 # count number of bits for 1205, will be 11 and subtract 1
sub = int("1"+"0"*temp,2) # the number that i am going to subtract from 1205
x = x-sub 
print(x)

# 2
temp = x.bit_length()-1
sub = int("1"+"0"*temp,2)
x = x-sub
print(x)

# 3
temp = x.bit_length()-1
sub = int("1"+"0"*temp,2)
x = x-sub
print(x)

# 4
temp = x.bit_length()-1
sub = int("1"+"0"*temp,2)
x = x-sub
print(x)

# 5
temp = x.bit_length()-1
sub = int("1"+"0"*temp,2)
x = x-sub
print(x)

