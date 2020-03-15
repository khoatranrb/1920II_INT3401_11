import numpy as np

class Node:
    def __init__(self, name=None):
        self.name = name


class Graph:
    def __init__(self, first_Node):
        self.list_Node = {first_Node:0}
        self.adj_matrix = np.array([0])
        self.linked= {first_Node:[], first_Node.name:[]}

    def add_Node(self, Node):
        if Node not in self.list_Node:
            self.linked[Node] = []
            self.linked[Node.name] = []
            n = len(self.list_Node)
            a1 = np.zeros((1,n))-1
            a2 = np.zeros((n+1,1))-1
            self.adj_matrix = np.vstack([self.adj_matrix, a1])
            self.adj_matrix = np.hstack([self.adj_matrix, a2])
            self.adj_matrix[-1][-1] = 0
            self.list_Node[Node] = n

    def set_edge(self, Node1, Node2, distance=0, direct=False):
        def _get_idx(Node):
            return self.list_Node[Node]
        self.adj_matrix[_get_idx(Node1)][_get_idx(Node2)] = distance
        if Node2 not in self.linked[Node1]:
            self.linked[Node1].append(Node2)
            self.linked[Node1.name].append(Node2)
        if not direct:
            self.adj_matrix[_get_idx(Node2)][_get_idx(Node1)] = distance
            if Node1 not in self.linked[Node2]:
                self.linked[Node2].append(Node1)
                self.linked[Node2.name].append(Node1)

    def _print_adj_matrix(self):
        print(self.adj_matrix)
    
    def _print_list_Node(self):
        for k,v in self.list_Node.items():
            print(k.name,':',v)

    def _print_linked(self):
        for k,v in self.linked.items():
            if type(k) is not str:
                print(k.name,':',[i.name for i in v])

class NodeTree:
    def __init__(self, name, way):
        self.linked = []
        self.name = name
        self.way = way
    def add_link(self, node):
        self.linked.append(node)
