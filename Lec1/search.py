import numpy as np
from data_struct import *

def DFS_search(graph, begin_node, target, way=[], find=[False]):
    way.append(begin_node.name)
    if find[0]:
        return None
    for i in graph.linked[begin_node]:
        if i.name not in way:
            if i==target:
                way.append(target.name)
                find[0] = True
                print(' --> '.join(way))
            else:
                DFS_search(graph, i, target,way)
                way.pop()

def BFS_search(graph, begin_node, target):
    root = NodeTree(begin_node.name, [begin_node.name])
    queue = [root]
    find = False
    while True:
        cur = queue.pop(0)
        cur_way = cur.way
        for i in graph.linked[cur.name]:
            way = cur_way.copy()
            way.append(i.name)
            node = NodeTree(i.name, way)
            cur.add_link(node)
            queue.append(node)
            if i==target:
                find = True
                result = node.way
                break
        if find:
            break
    print(' --> '.join(result))
