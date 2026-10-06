
'''

for constraints,  num of queries for all test cases combined can go up to 2x10^6
This means that each 1,2 and 3 type query must be performed strictly within  O(1) to O(logn)

Query type 1:
From What I understand
b = len(s)+x  c is the number of integers less than b that give math.gcd(b,c) = 1, that means f(b) =number of ntegers that are not divisible by b
example:
if len(s) is 5, x=4 then b=9 find all c where g(9,c)=1
in case of b=9, gcd(9,1)=1, gcd(9,2) = 1, gcd(9,4) = 1, gcd(9,5)=1, gcd(9,7 )=1, gcd(9,8)=1
that means f(9) = 6, y=f(9)%26 = 6, nextLetter = chr(y+1+97) = chr(104) = "f"


Query type 3:
for any string, distinceNumberOfPalindromes <= len(s)
example1: s="aaaaa", distinctPalindromes = {a,aa,aaa,aaaa,aaaaa}, output:5
example2: s="abcde", distinctPalindromes = {a,b,c,d,e}, output:5
example3: s="abcda", distinctPalindromes = {a,b,c,d}, output: 4
example4: s="ababa", distinctPalindromes = {a,b,aba,bab,ababa}, output:5
example5: s="abab", distintPalindromes = {a,b,bab,aba}, output: 4

'''