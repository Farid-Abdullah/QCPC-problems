
# despite all the effort, this still is O(qN)in worse possible test case
#  where q>=3x10^5 and n=6X10^5, this will get TLE for sure. Otherwise the dfs function
# has a pruning condition that will aggressively cut down complexity. 

# in test case where theString= "aaaa.....aaaaa" (max number of a's) and say each query is "aaa.aaaaa" all a's
# then there can't be any pruning done, therefore TLE


import sys
sys.setrecursionlimit(600000) # because n could be up to 6X10^5

#  Trie data structure for the list of strings:
class TrieNode:
    def __init__(self):
        self.next = {}
        self.ended = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,string):
        cur = self.root
        for character in string:
            if character not in cur.next:
                cur.next[character] = TrieNode()
            cur = cur.next[character]
        # the loop ends means string ended here, so:
        cur.ended = True

def dfs_trie_search(current, target, parent, current_trie_node):
        character = theString[current]
        
        # THE PRUNING
        if character not in current_trie_node.next:
            return False
            
        next_trie_node = current_trie_node.next[character]
    
        # path reached( or dfs completed)
        if current == target:
            return next_trie_node.ended
            
        # THE RECURSION: Continue tree DFS, passing the updated Trie node
        for neighbor in all_nodes[current]:
            if neighbor != parent: # e.g. in 6:[3] item, neighbor is 3,the list all_nodes[3] will have 6 again, this condition will eliminate this cicular logiic
                if dfs_trie_search(neighbor, target, current, next_trie_node):
                    return True
                    
        return False
#input:
# Creating the given tree, as a dictionary where keys are the nodes, and values are list of neighbor nodes.

t = int(input())

for test in range(t):
    n,m = map(int, input().split())
    all_nodes = {}
    for _ in range(n-1):
        u,v = map(int, input().split())
        u,v = u-1,v-1
        if all_nodes.get(u):
            all_nodes[u].append(v)
        else:
            all_nodes[u] = [v]
        if all_nodes.get(v):
            all_nodes[v].append(u)
        else:
            all_nodes[v] = [u]
    theString = input()
    trie = Trie()
    for _ in range(m):
        trie.insert(input())

    q = int(input()) # number of queries

    for _ in range(q):
        u,v = map(int, input().split())
        u,v = u-1,v-1

        # prepare the string or just pass startring and ending node to search:
        # I decided to go for passing start and ending nodes to the trie search
        if dfs_trie_search(u, v, -1, trie.root):
            print("YES")
        else:
            print("NO")



