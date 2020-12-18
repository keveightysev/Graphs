class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Cannot create edge from vertices')

    def get_parent(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

    if graph.vertices[starting_node] == set():
        return -1

    queue = Queue()

    earliest = (starting_node, 0)

    queue.enqueue(earliest)

    while queue.size():
        current = queue.dequeue()

        if (current[0] < earliest[0] and current[1] == earliest[1]) or current[1] > earliest[1]:
            earliest = current

        parents = graph.get_parent(current[0])

        for parent in parents:
            queue.enqueue((parent, current[1] + 1))

    return earliest[0]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 3))
