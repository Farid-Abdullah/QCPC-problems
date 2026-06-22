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

'''

# solution plan:
'''
distance = 0 
calculate all the prime factors for all the nodes,
create a dictionary where key is primeFactor, and value is list of nodes_id, where node_id is the reference to node in the tree.
construct the tree using the given edges.
    
'''
class Node:
    _registry = {} # class attribute, onl editable inside the class

    # might not be relevant to the problem but: some ideas about __new__ and using hasattr in __init__ to make sure no duplicated instances get made.

    def __init__(self, nodeId):
    
        self.linkedTo = set()
       

    def link(self ,node):
        self.linkedTo.add(node)

    @classmethod
    def get_or_create(cls, nodeId):
        if nodeId not in cls._registry:
            cls._registry[nodeId] = cls(nodeId)
        return cls._registry[nodeId]





n = 3
nList = [2,3,4]
