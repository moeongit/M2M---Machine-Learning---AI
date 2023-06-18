import turtle
from collections import defaultdict
from queue import SimpleQueue
from graph_utils import Graph, Node


def bfs(source: Node):
    visited = defaultdict(bool)
    path = []
    q = SimpleQueue()
    q.put(source)
    visited[source] = True
    path.append(source)

    while not q.empty():
        current = q.get()
        for neighbor in current.neighbors:
            if visited[neighbor] == False:
                q.put(neighbor)
                visited[neighbor] = True
                path.append(neighbor)
    return path    


def bfs_target(source: Node, target: Node):
    visited = defaultdict(bool)
    q = SimpleQueue()
    q.put(source)
    visited[source] = True
    while not q.empty():
        cur_node = q.get()
        if cur_node == target:
            return True
        
        for neighbor in cur_node.neighbors:
            if visited[neighbor] == False:
                q.put(neighbor)
                visited[neighbor] = True
    return False



graph = Graph('graph2.txt', undirected = False)
nodes = graph.nodes

path = bfs(nodes['1'])
# target = bfs_target(nodes['0'], nodes['6'])


# print(target)
graph.draw_graph()
graph.draw_path(path, draw_lines=False)
turtle.done()