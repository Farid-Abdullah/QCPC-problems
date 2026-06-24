'''
Provel H. GCTree
Given a tree with n nodes, what is the maximum ditance between any two nodes, with values i and j, provided that their greatest
common divisor  (gcd(i,j)) is greater than 1?

Understanding the question is the hardest part.
ok, solving it is even harder

input:
example1:
3   # number of nodes/vertices in the tree
2 3 4  # the nodes with its values
2 1  # 2nd node (which has the value 3) has edge with the first node. (having an edge between nodes means they are connected)
3 1  # 3rd node (which has the value 4) has edge with the first node.
output: 2       # because node 1 and node 3 with values 2 and 4, share a gcd>1, and also share an edge(both are connected). so distance = node1 to node3 = 2 counting the nodes.

example2:

3
3 2 4
2 1
3 1
output: 3       # 2nd and 3rd node share gcd>1. distance = node2 to node1 to node3 = 3

testCase:
n = 3
nList = [5,6,7,4,3,2,3,9,2,1,4,3,5]
edges = [
    [1, 4], [2, 4],[3,4],
    [4,5], [5,6],[6,8],[7,8],[8,9],[9,10],
    [8,11],[12,11],[13,11]
]

'''

# solution plan:
'''
get smallest prime factors for all nodes, from that, calculate all the unique prime factors of that node.
create a dictionary grouping all
    
'''
class Node: # id, set of prime factors and refs to other nodes.

    _registry = {} # class attribute, onl editable inside the class

    # might not be relevant to the problem but: some ideas about __new__ and using hasattr in __init__ to make sure no duplicated instances get made.

    def __init__(self, nodeId, val):
    
        self.linkedTo = []
        self.pf = allPrimeFactors(val)
        createPrimeToNodes(self,self.pf)
       

    def link(self ,node):
        self.linkedTo.append(node)

    @classmethod
    def get_or_create(cls, nodeId, val):
        if nodeId not in cls._registry:
            cls._registry[nodeId] = cls(nodeId, val)
        return cls._registry[nodeId]




def spf_array(n=100000):
    '''create a list where elements are smalles prime factors for given index, index will be treated like a number'''
    spf = [i for i in range(n + 1)] # every number is its own smalles prime factor in the beginning.

    p = 2
    n_root = int(n**0.5)
    while p<=n_root:
        if spf[p] == p: # in sieve we do primes[p], which gives true for primes and false for the rest, but here if index ==value, means we are on a prime
            for i in range(p*p, n+1, p):
                if spf[i] == i: # if the multiples of the prime are not replaced by a smaller prime number yet
                    spf[i] = p # for example index 15 will store 3, cuz 3 is smallest prime for 15
        p+=1
    
    return spf

spf = spf_array()
def allPrimeFactors(num, spf=spf_array()):
    '''get all prime factors for a given num using spf_array, start with smallest prime factor'''
    pf = set()
    while num>1: # just like manual prime factorizing steps, we stop when we reach 1  or 0
        pf.add(spf[num])
        num = num//spf[num] 
    return pf

n = 3
nList = [2,3,4]
edges = [
    [2,1],[3,1]
]


primeToNodes = {} # dicationary where keys will be all possible prime numbers using the given nodes, value will be set of all nodes whose value has the kay as a prime factor
def createPrimeToNodes(node,val):
    global primeToNodes
    for p in node.pf:
        primeToNodes.setdefault(p, set()).add(node)


for edge in edges: # creating the tree, and creating the primeToNodes dictionary at the same time using edges
    node1 = Node.get_or_create(edge[0]-1, nList[edge[0]-1])
    node2 = Node.get_or_create(edge[1]-1, nList[edge[1]-1])
    node1.link(node2)
    node2.link(node1)


def dfs(node, temp_set, max_dis):
    ''''''
    visited.add(node)
    max_child_distance = 0
    for n in node.linkedTo:
        if neighbor i
    

print(primeToNodes)
max_dis = -1
for prime, node_set in primeToNodes.items():
    if len(node_set)<2:
        continue

    temp_set = node_set.copy()
    for root in temp_set: # must calculate distance using every node. just doing 1 will miss cases
        visited = set()
        path_length = dfs(root,temp_set,visited)

        if path_length>max_dis:
            max_dis = path_length