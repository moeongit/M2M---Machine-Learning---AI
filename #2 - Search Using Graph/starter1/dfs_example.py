import turtle
from typing import List, Tuple
from graph_utils import Graph, Node

def dfs_non_recursive(source: Node, goal) -> Tuple[List[Node], bool]:
    # Performs depth-first search on a graph
    path = []
    to_visit = [source]
    while len(to_visit) != 0: 
        current = to_visit.pop()

        if current in path:
            continue
        
        path.append(current)

        if current == goal:
            return path, True
        for neighbor in current.neighbors:
            to_visit.append(neighbor)

    return path, False

graph = Graph("dfs-graph.txt", undirected=False)
nodes = graph.nodes


dfs_path, found = dfs_non_recursive(nodes['A'], nodes['E'])
print(found)
graph.draw_graph()
graph.draw_path(dfs_path, draw_lines = False)
turtle.done()