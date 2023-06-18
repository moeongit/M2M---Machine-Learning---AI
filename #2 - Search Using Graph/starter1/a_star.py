"""We will use the A* algorithm to simulate a very simple GPS system that finds
a path between to points.

This introduces the concepts of edge weights. In our graph, the weight of each
edge is the distance between the two points.

References:
- https://en.wikipedia.org/wiki/A*_search_algorithm
"""

from collections import defaultdict
from queue import PriorityQueue
import turtle
from typing import Callable, List, Optional, Tuple, TypeVar

import sys
sys.path.append('.')

from graph_utils import Node, Graph

# Generic type restricted to any subclass of `Node`
GeneralNode = TypeVar('GeneralNode', bound=Node)


def reconstruct_path(came_from: dict,
                     current: GeneralNode) -> List[GeneralNode]:
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path = [current] + total_path
    return total_path


NodeType = TypeVar('NodeType')
Heuristic = Callable[[NodeType, NodeType], float]


def a_star(start: GeneralNode, goal: GeneralNode,
           h: Heuristic[GeneralNode]) -> Optional[List[GeneralNode]]:
    """A* finds a path from `start` to `goal`.
    
    `h` is the heuristic function. `h(n, goal)` estimates the cost to reach
    `goal` from node `n`.
    """
    open_set: PriorityQueue[Tuple[float, GeneralNode]] = PriorityQueue()

    # For node n, came_from[n] is the node immediately preceding it on the
    # cheapest path from start to n currently known.
    came_from = dict()

    # For node n, g_score[n] is the cost of the cheapest path from start to n
    # currently known.
    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0

    h_initial = h(start, goal)

    # For node n, f_score[n] = g_score[n] + h(n, goal). f_score[n] represents
    # our current best guess as to how short a path from start to finish can be
    # if it goes through n.
    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = h_initial

    open_set.put((h_initial, start))

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, weight in current.get_weighted_neighbors():
            # tentative_g_score is the distance from start to the neighbor
            # through current
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                # This path to neighbor is better than any previous one. Record it!
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h(neighbor, goal)
                if neighbor not in open_set.queue:
                    open_set.put((f_score[neighbor], neighbor))


if __name__ == '__main__':
    graph = Graph('week-2/graph2.txt', undirected=True)
    nodes = graph.nodes

    """
    We use the distance between the two points as the heuristic. This tells the
    algorithm that moving to a point which is closer to the goal is more
    desirable than moving to a point that is further from it.

    Note that our graph additionally includes the distance between each two
    points as the weight of that edge. These weights are what informs A* to
    prefer shorter paths to the goal, and this makes our system behave more like
    a GPS.
    """
    h = graph.calc_distance  # lambda _, __: 0
    path = a_star(nodes['1'], nodes['10'], h)

    graph.draw_graph()
    if path:
        graph.draw_path(path)

    turtle.done()
