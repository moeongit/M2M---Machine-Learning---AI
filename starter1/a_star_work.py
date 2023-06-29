from collections import defaultdict
from queue import PriorityQueue
import turtle
from graph_utils import Graph, Node


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path = [current] + total_path
    return total_path

def a_star(start, goal, h):
    # A* Finds the shortest path from 'start' to 'goal'.
    # "h" is the heuristic function. 'h(n, goal)' estimates the cost to reach
    # 'goal' from node 'n'.

    open_set = PriorityQueue()

    came_from = {}
    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0

    f_score = defaultdict(lambda: float("inf"))
    distance_initial = h(start, goal)
    f_score[start] = distance_initial

    open_set.put((f_score[start], start))

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor, weight in current.get_weighted_neighbors():
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                # This path is better than any previous one
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h(neighbor, goal)
                came_from[neighbor] = current
                if neighbor not in open_set.queue:
                    open_set.put((f_score[neighbor], neighbor))

if __name__ == "__main__":
    graph = Graph("graph2.txt", undirected=True)
    nodes = graph.nodes

    h = graph.calc_distance
    path = a_star(nodes["1"], nodes["7"], h)

    graph.draw_graph()
    graph.draw_path(path)
    turtle.done()