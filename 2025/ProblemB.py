
# 1d dp approach + Trie data structure, but still O(n^2) if s = "a"*10^5 and Trie is filled with "a"

class TrieNode:
    def __init__(self):
        self.next = {}

        self.ended = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,dstring):
        cur = self.root
        for char in dstring:
            if char not in cur.next:
                cur.next[char] = TrieNode()
            cur = cur.next[char]
        cur.ended +=1



# input:
n = int(input())
trie = Trie() # this will hold all thte strings in the dictionary
for _ in range(n):
    trie.insert(input())
m = int(input())
s = input()


#solution:
dp = [0]*(m+1) # array length of s
dp[0] = 1 # base case for empty string
MODUL = 10**9 + 7 #since final answer mush be taken to %(10^9 +10) as per question.


for i in range(0,m):
    if dp[i]>0:
        cur = trie.root
        for j in range(i,m):
            if s[j] not in cur.next:
                break
            cur = cur.next[s[j]]
            if cur.ended:
                dp[j+1] = ((dp[i]*cur.ended)+dp[j+1]) % MODUL # multiplying by cur.ended to account for duplicated combinations
print(dp[-1])


    