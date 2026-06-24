import sys
sys.setrecursionlimit(300000)

class Node:
    _registry = {}

    def __init__(self, nodeId, val):
        self.id = nodeId
        self.linkedTo = []
        self.pf = allPrimeFactors(val)
        createPrimeToNodes(self, self.pf)
        
        # New attributes to track position in the main tree
        self.depth = 0
        self.parent = None

    def link(self, node):
        self.linkedTo.append(node)

    @classmethod
    def get_or_create(cls, nodeId, val):
        if nodeId not in cls._registry:
            cls._registry[nodeId] = cls(nodeId, val)
        return cls._registry[nodeId]


def spf_array(n=100000):
    spf = [i for i in range(n + 1)]
    p = 2
    n_root = int(n**0.5)
    while p <= n_root:
        if spf[p] == p:
            for i in range(p*p, n+1, p):
                if spf[i] == i:
                    spf[i] = p
        p += 1
    return spf

spf = spf_array()

def allPrimeFactors(num, spf=spf):
    pf = set()
    while num > 1:
        pf.add(spf[num])
        num = num // spf[num]
    return pf


primeToNodes = {} 
def createPrimeToNodes(node, val):
    global primeToNodes
    for p in node.pf:
        primeToNodes.setdefault(p, set()).add(node)


# Test Data Setup (Your 13-node custom example)
n = 3

nList = [2,3,15]

edges = [

    [2,1],[3,1]

]

Node._registry.clear()

for edge in edges:
    node1 = Node.get_or_create(edge[0]-1, nList[edge[0]-1])
    node2 = Node.get_or_create(edge[1]-1, nList[edge[1]-1])
    node1.link(node2)
    node2.link(node1)


# --- 1. INITIAL DFS TO MEASURE THE MAIN TREE STUCTURE ---
def setup_tree(node, parent, current_depth):
    node.depth = current_depth
    node.parent = parent
    for neighbor in node.linkedTo:
        if neighbor != parent:
            setup_tree(neighbor, node, current_depth + 1)

# Start setup from the first node in the registry
root_node = Node._registry[0]
setup_tree(root_node, None, 1)


# --- 2. HELPER TO FIND TRUE DISTANCE VIA LCA ---
def get_distance(node1, node2):
    """Calculates the number of nodes on the simple path between node1 and node2"""
    u, v = node1, node2
    dist = u.depth + v.depth
    
    # Lift the deeper node up to match depths
    while u.depth > v.depth:
        u = u.parent
    while v.depth > u.depth:
        v = v.parent
        
    # Lift both up together until they meet at their Lowest Common Ancestor
    while u != v:
        u = u.parent
        v = v.parent
        
    lca = u
    # Total vertices formula: depth(u) + depth(v) - 2 * depth(LCA) + 1
    return dist - 2 * lca.depth + 1


# --- 3. FINDING MAX DISTANCE ---
max_dis = 0
for node_obj in Node._registry.values():
    if len(node_obj.pf) > 0:
        max_dis = 1

# Process each prime group
for prime, node_set in primeToNodes.items():
    if len(node_set) < 2:
        continue
    
    nodes_list = list(node_set)
    
    # A brilliant property of tree subsets: 
    # To find the max distance pair in a set, pick an arbitrary node, 
    # find the farthest node from it (A), then find the farthest node from A (B).
    
    # Find farthest node 'A' from an arbitrary starting node
    start_node = nodes_list[0]
    farthest_node_A = start_node
    max_d = 0
    for target in nodes_list:
        d = get_distance(start_node, target)
        if d > max_d:
            max_d = d
            farthest_node_A = target
            
    # Find farthest node 'B' from 'A'
    max_path_for_prime = 0
    for target in nodes_list:
        d = get_distance(farthest_node_A, target)
        if d > max_path_for_prime:
            max_path_for_prime = d
            
    if max_path_for_prime > max_dis:
        max_dis = max_path_for_prime

print(f"Final Answer: {max_dis}")


# second solution:
print()
print()
def solve():
    # Fast I/O
    
    n = n = 13
    
    # 1-indexed node values
    node_values = [0] + [5, 6, 7, 4, 3, 2, 3, 9, 2, 1, 4, 3, 5]
    
    # Construct standard adjacency list
    adj = [[] for _ in range(n + 1)]
    idx = n + 1
    edges = [
    [1, 4], [2, 4], [3, 4],
    [4, 5], [5, 6], [6, 8], [7, 8], [8, 9], [9, 10],
    [8, 11], [12, 11], [13, 11]
]
    for i in edges:
        u = i[0]
        v = i[1]
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # Step 1: Precompute Smallest Prime Factors (SPF) Sieve
    MAX_V = 100000
    spf = list(range(MAX_V + 1))
    for p in range(2, int(MAX_V**0.5) + 1):
        if spf[p] == p:
            for i in range(p * p, MAX_V + 1, p):
                if spf[i] == i:
                    spf[i] = p

    # Map each prime factor to the list of node IDs containing it
    prime_to_nodes = [[] for _ in range(MAX_V + 1)]
    for node_id in range(1, n + 1):
        val = node_values[node_id]
        while val > 1:
            p = spf[val]
            prime_to_nodes[p].append(node_id)
            while val % p == 0:
                val //= p

    # Step 2: Tree Flattening (DFS Order) & Binary Lifting Setup for LCA
    LOGN = 18
    depth = [0] * (n + 1)
    up = [[0] * LOGN for _ in range(n + 1)]
    tin = [0] * (n + 1)
    timer = 0

    def dfs_setup(u, p, d):
        nonlocal timer
        timer += 1
        tin[u] = timer
        depth[u] = d
        up[u][0] = p
        
        for i in range(1, LOGN):
            up[u][i] = up[up[u][i-1]][i-1]
            
        for v in adj[u]:
            if v != p:
                dfs_setup(v, u, d + 1)

    # Initialize the structural properties of the main tree
    dfs_setup(1, 1, 1)

    # O(log N) Lowest Common Ancestor calculation
    def get_lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        # Lift u to the same depth as v
        for i in range(LOGN - 1, -1, -1):
            if depth[u] - (1 << i) >= depth[v]:
                u = up[u][i]
        if u == v:
            return u
        # Lift both until right below LCA
        for i in range(LOGN - 1, -1, -1):
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        return up[u][0]

    # Calculate actual path distance (number of vertices on simple path)
    def get_dist(u, v):
        lca = get_lca(u, v)
        return depth[u] + depth[v] - 2 * depth[lca] + 1

    # Initialize global maximum distance
    global_max_distance = 0
    for node_id in range(1, n + 1):
        if node_values[node_id] > 1:
            global_max_distance = 1

    # Step 3: Compute maximum subset distance per prime
    for p in range(2, MAX_V + 1):
        nodes = prime_to_nodes[p]
        if len(nodes) < 2:
            continue
            
        # Optimization Property: Sorting nodes by their DFS entry time (tin)
        # allows us to find the diameter of a subset of tree nodes efficiently.
        nodes.sort(key=lambda x: tin[x])
        
        # Pass 1: Find the node farthest from the first node in DFS order
        farthest_node = nodes[0]
        max_d = 0
        for node in nodes:
            d = get_dist(nodes[0], node)
            if d > max_d:
                max_d = d
                farthest_node = node
                
        # Pass 2: Find the true maximum diameter of this subset from that farthest point
        for node in nodes:
            global_max_distance = max(global_max_distance, get_dist(farthest_node, node))

    print(global_max_distance)

solve()