
# dp approach, but still O(n^2) which will likely cause TLE :(
# according to Gemini, I must use Trie data structure to eliminate the loop "for word in All"
# I don't yet know what Trie is.

# input:
n = int(input())
All = []
for _ in range(n):
    All.append(input())
m = int(input())
s = input()

#solution:
dp = [0]*(m+1) # array length of s
dp[0] = 1 # base case for empty string
MODUL = 10**9 + 7 #since final answer mush be taken to %(10^9 +10) as per question.


for i in range(0,m):
    if dp[i]>0:
        for word in All:
            if s.startswith(word,i): # word matches s starting at index i
                L =len(word)
                dp[i+L] = (dp[i]+dp[i+L]) % MODUL
print(dp[-1])

    
    