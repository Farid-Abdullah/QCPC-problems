

import sys

all_input = sys.stdin.read().split()


class TrieNode:
    def __init__(self):
        self.children = {}
        self.ended = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.possible = "NO"
    def insert(self, word):
        node = self.root
        i = 0
        while i<len(word) and node.ended ==0 and len(node.children)<=1:
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
        
            node = node.children[word[i]]
            i+=1
        node.ended += 1
    def commonSuffix(self):
        node = self.root
        suffix = ""
        while len(node.children)==1 and node.ended == 0:
  
            key = list(node.children.keys())[0]
            suffix += key
            node = node.children[key]
        if suffix == "":
            print("NO")
        else:
            print("YES")
            print(suffix[::-1])
trie = Trie()
for w in all_input[1:]:
    trie.insert(w[::-1])


trie.commonSuffix()   