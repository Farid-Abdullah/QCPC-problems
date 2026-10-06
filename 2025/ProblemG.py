



def bruteforce(): # uses set for storage
    s = set()
    q = int(input())
    for _ in range(q):
        
        t,x = map(int, input().split())
        if t == 1:
            s.add(x)
        elif t == 2:
            s.remove(x)
        else: # the main problem focus return max(a&x) count(max(a&x))
            count = 0
            maxAnd = float("-inf")
            for i in s:
                op = i&x
                if op ==maxAnd:
                    count+=1
                    
                elif op > maxAnd:
                    count = 1
                    maxAnd = op
            print(max(maxAnd,0),count)
#bruteforce()


class TrieNode:
    def __init__(self):
        self.next = {}

        self.freq = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,bit_string):
        # what if they try to add the same number again? in sets data structure that would be ignored, but in this implementation that will add extra freq.
        cur = self.root
        for i in range(len(bit_string)-1, -1,-1) :
            if bit_string[i] not in cur.next:
                cur.next[bit_string[i]] = TrieNode()
            cur = cur.next[bit_string[i]]
            cur.freq +=1
            print(cur.freq)
    def remove(self, bit_string):  # simple since it is gauranteed that the number exists in the set
        cur = self.root
        for i in range(len(bit_string)-1, -1,-1) :
            cur = cur.next[bit_string[i]]
            cur.freq -=1
            print(cur.freq)
    def calMax(self,xbit_string):
        cur = self.root
        m = float("-inf")
        bit_ans = ""
        count = 0
        for i in range(len(xbit_string)-1, -1,-1):
            if xbit_string[i]=="1" and "1" in cur.next:
                bit_ans = "1" + bit_ans # concatenating in reverse, because trie has bits in revers
                count = cur.next["1"].freq
            else:
                bit_ans = "0" +bit_ans
            cur = cur.next["0 or 1"] # got lost here, verdict: Trie was not possible to begin with


def trieMethod(): # Wrong: uses Trie for storing bitString in reverse
    q = int(input())
    trie = Trie()
    for _ in range(q):
        t, x = input().split()
        t = int(t)
        x = bin(int(x))[2:] # removing the ob part from binary string


        if t == 1:
            trie.insert(x)
            
        elif t == 2:
            trie.remove(x)
        else: # the main problem focus return max(a&x) count(max(a&x))
            count = 0
            maxAnd = float("-inf")
            for i in s:
                op = i&x
                if op ==maxAnd:
                    count+=1
                    
                elif op > maxAnd:
                    count = 1
                    maxAnd = op
#trieMethod() #Bad Bad
def solution2():

    q = int(input())

    
    dict1s = {} # max binary element can't be more than 19 per constraints
    s = set()
    for _ in range(q):
        t,x = map(int, input().split())

        
        if t ==1:
            if x not in s:
                s.add(x)
                x = f"{x:20b}"
                leading = False
                for i in range(len(x)-1,-1,-1): # O(20) 
                    if x[i]=="1":
                        if i in dict1s:
                            dict1s[i][0]+=1
                            
                        else:
                            dict1s[i] = (1, False)
                        last1 = i
                dict1s[last1][1] = True
        elif t == 2:
            s.remove(x)
            x = bin(x)[2:]
            # I'll do this logic later
        elif t == 3:
            if s == set(): # incase empty
                print("0 0")
                continue
            x = f"{x:20b}"
            count = float("inf")
            maxBin = ""
            flag = False
            for i in range(len(x)-1,-1,-1):
                
                if x[i]=="1" and i in dict1s:
                    if dict1s[i][1] or not flag:
                        count = min(count, dict1s[i])
                        maxBin = "1"+maxBin
                    else:
                        flag = True
                else:
                    maxBin = "0" +maxBin
            if count == float("inf"):
                count = 0
            print(int(maxBin,2), count)



#solution2() #Also bad attempt, fails at simplest test case when s-{8,2}, t=3 x=10 prints 10 1 but it should pring 8 1