from data_struct import *
from search import *

K = Node('K')
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
I = Node('I')
G = Node('G')

S = Node('S')
P = Node('P')
Q = Node('Q')
H = Node('H')
R = Node('R')

# Build graph 1
X = Graph(first_Node = A)

X.add_Node(B)
X.add_Node(C)
X.add_Node(D)
X.add_Node(E)
X.add_Node(F)
X.add_Node(G)
X.add_Node(K)
X.add_Node(I)


X.set_edge(A, B, direct=1)
X.set_edge(A, C, direct=1)
X.set_edge(A, D, direct=1)

X.set_edge(B, I, direct=1)
X.set_edge(B, G, direct=1)

X.set_edge(C, F, direct=1)
X.set_edge(C, E, direct=1)

X.set_edge(D, F, direct=1)
X.set_edge(D, C, direct=1)

X.set_edge(E, K, direct=1)
X.set_edge(E, G, direct=1)

X.set_edge(F, K, direct=1)

X.set_edge(I, G, direct=1)

# Build graph 2
Y = Graph(first_Node = A)

Y.add_Node(B)
Y.add_Node(C)
Y.add_Node(D)
Y.add_Node(E)
Y.add_Node(F)
Y.add_Node(G)
Y.add_Node(P)
Y.add_Node(Q)
Y.add_Node(S)
Y.add_Node(H)
Y.add_Node(R)

Y.set_edge(B, A, direct=1)

Y.set_edge(C, A, direct=1)

Y.set_edge(D, B, direct=1)
Y.set_edge(D, C, direct=1)
Y.set_edge(D, E, direct=1)

Y.set_edge(E, H, direct=1)
Y.set_edge(E, R, direct=1)

Y.set_edge(F, C, direct=1)
Y.set_edge(F, G, direct=1)

Y.set_edge(H, P, direct=1)
Y.set_edge(H, Q, direct=1)

Y.set_edge(S, D, direct=1)
Y.set_edge(S, P, direct=1)
Y.set_edge(S, E, direct=1)

Y.set_edge(P, Q, direct=1)

Y.set_edge(R, F, direct=1)


if __name__=="__main__":
    DFS_search(X, A, K)
    DFS_search(Y, S, G)
#     print('')
    BFS_search(Y, S, G)
    BFS_search(X, A, K)
    # BFS(X,A)
