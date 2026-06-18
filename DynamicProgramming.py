

# Dynamic programming
# Overview:
'''
DP is an algorithmic optimization techinique used to solve complex problems by breaking them down into
simpler, overlapping subproblems. Instead of repeating calcualtions for thse subproblems, DP stores
the computed answer in memory, thus reducing exponential time complexities down to polynomial for memory
trade-off.

Two approches:
1. recursive memoization:  Top-down, recursive, stores results in array/hashmap(dict) called cache.

2. Tabulation:Bottom-up, iterative, solves from small to large, fills dataTable sequentually to store cache
'''

# example 1 (classic): Fibonacci sequence calculation

def fib_memo(n, cache={}):
    '''solving fibonacci(n) using recursive memoization, or Top-down approach'''
    
    if n in cache:  # if fib(n) was already done, it is stored in cache like: {n:result}
        return cache[n] # therefore just return  the previously done operation instead of repeating fib(n) again
    if n<=2: # base case
        return 1
    cache[n] = fib_memo(n-1,cache) + fib_memo(n-2, cache) # normally: return f(n-1)+f(n-2)
    return cache[n]

def fib_tab(n):
    '''solving fibonacci(n) using tabulation, or bottom-up approach.'''
    if n<=2: # not a base case, because this is not recursion
        return 1
    dp = [0] * (n+1)  # 1D array of size n+1 to store solution to fib(n) from small problems to large. e.g: fib(1),fib(2),fib(3)
    dp[1] = 1 # result of fib(1)
    dp[2] = 1 # result of fib(2), both will be used to build up the  solution for 3,4,5,....n
    
    for i in range(3,n):
        dp[i] = dp[i-1] + dp[i-2] # critical part, we are using previously solved fib nums to solve new ones
    return dp[n] # the last number at the last index will be the actual result of fib(n)

# example 2: leetcode problem 10, Regular expression matching
'''
Overview:
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
Return a boolean indicating whether the matching covers the entire input string (not partial).
examples: s= "aa", p = "a", output:false || s="aa",p="a*", Output:true || s=ab, p= ".*" || output: true
cases where greedy string construction fails: s="aaa" p="a*a" output:true || s="aaa" p=ab*a*c*a output:true
'''
# solving it using DP top-down approach, we need to consider the following:
"""
We need two pointers, i and j, when will iterate over s the other over p.
the problem should be broken down into small subproblems,
and result stored in cache = {} for those subproblems, where keys are tuples (i,j) and values are bool
new recursive function: match(i,j) the recursive function that will try to prove if s[i:]==p[j:]
base case: when j==len(p) (out of bounds) and i==len(s) return true, else return false.

when p[j+1] is '.' or normal char: cache[(i,j)] = p[j]==s[i] and match(i+1, j+1)
when p[j+1] is '*':
    two cases:  skip or useOnce
    skip = match(i, j+2) which means given a* we will use 'a' zero times
    useOnce = p[j]==s[i] and match(i+1, j), which means given a* will check "a" against s[i] once, and check if we should do it again.
                ^ if p[j] and s[i] are not the same, match(i+1, j) is not called and not needed to be called.
    both 'skip' and 'useOnce' variable are booleans, and we store it in our cache for (i,j) by:
    cache[(i,j)] = skip or useOnce
                                
    then the base case will backtrack the boolean.
"""
def isMatch(s,p):
    
    if "*" not in p:
        if len(s) != len(p):
            return False
        for i in range(len(s)):
            if s[i] != p[i] and p[i] != '.':
                return False
            
        return True
    cache = {}
    
    def match(i,j):
        if (i,j) in cache: # cache lookup for previously excecuted stats
            return cache[(i,j)]
        if j==len(p):
            return i==len(s) # if both j and i are len of p and s respectively, then should return true
        currentMatch = i<len(s) and (p[j] == s[i] or p[j] == ".")
        
        if (j+1)<len(p) and p[j+1]=="*": # p[j+1] is "*" so either skip p[j] or use it once
            skip = match(i,j+2)
            useOnce = currentMatch and match(i+1, j) 
            result = skip or useOnce
            
            
        else: # normal single checkup into cache
            result = currentMatch and match(i+1,j+1)
        cache[(i,j)] = result
        return result
    return match(0,0)



print(isMatch("aaa","a*a"))

print(isMatch("mississippi", "mis*is*p*."))
print(isMatch("mississippi", "mississ.ppi"))
            
            
            
            
        
            
        




















        
        
    




    
