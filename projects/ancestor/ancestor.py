class Queue():   # FIFO   or LILO
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)      # REMEBER periodic resizing
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)    # this is O(n)
        else:
            return None
    def size(self):
        return len(self.queue)


class Graph:
    
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # just add new dict entry
        self.vertices[vertex_id] = set()

        pass  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        pass  # TODO
    # both vertices have to exist to make connection(e.g. directed edge)

        if v1 in self.vertices and v2 in self.vertices:
            # print(f' type(vertices) is {type(self.vertices)}')
            self.vertices[v1].add(v2)  # using set .add() method to append
        else:
            # print(f'ERROR: vertex {v1} or {v2} does not exist')     
            raise ValueError("Vertex not yet created")
            # print(f'ERROR: vertex {v1} or {v2} does not exist')

    # get_parent  will find vertices connected (like get_neighbors hmmm )

    def show_connected_vertices(self):
        print(f' Family Tree')
        for item in self.vertices:
            if len(self.vertices[item]) == 0:
                print(f' \t item {item} has no ancestors')

            for set_item in self.vertices[item]:
                print(f'  Vertex {item} is child(has edge) to vertice(s) : {self.vertices[item]}')
                break
            

    def get_ancestor(self, v):
        # if v exists in dict, return set            
        if v in self.vertices:
            # print(f" v found is {v}")
            return self.vertices[v]
        else:
            raise ValueError(f" Cannot locate ancestor called {v}")    

graph = Graph()


def earliest_ancestor(ancestors, starting_node):
    
    # build graph from ancestors
    for v_pair in ancestors:
        graph.add_vertex(v_pair[0])
        graph.add_vertex(v_pair[1])
        # graph.add_edge(v_pair[0], v_pair[1])
        # print(f' v_pair[0]  {v_pair[0]}')
    
    for v_pair in ancestors:
        graph.add_edge(v_pair[1], v_pair[0])

    # current_ancestor = -1   # need for debugging( variable ref before assignment )

    q = Queue()                         # Create queue
    visited = set()                     # create visited set
    q.enqueue([starting_node])          # enqueue starting_node

    while q.size() > 0:             # while queue NOT empty
        print(f'  queue NOW {q.queue}')
        path = q.dequeue()                # dequeue first PATH vertices
        print(f'  path {path}')
        current_ancestor = path[-1]       # get last item in path
        # print(f' \t current_ancestor {current_ancestor}')

        if current_ancestor not in visited:            # check if NOT visited
            visited.add(current_ancestor)               # add v to visited

        for v in graph.get_ancestor(current_ancestor):
            print(f' current v is {v}')
            path_c = path[:]
            path_c.append(v)
            q.enqueue(path_c)

    # At this point, there are no more ancestors, so most recent current_ancestor is earliest_ancestor
    
    if current_ancestor == starting_node:
        return  -1
    else:
        # print(current_ancestor)
        return current_ancestor        
    

############
"""
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
"""
"""      
        test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
        self.assertEqual(earliest_ancestor(test_ancestors, 1), 10)
        self.assertEqual(earliest_ancestor(test_ancestors, 2), -1)
        self.assertEqual(earliest_ancestor(test_ancestors, 3), 10)
        self.assertEqual(earliest_ancestor(test_ancestors, 4), -1)
        self.assertEqual(earliest_ancestor(test_ancestors, 5), 4)
        self.assertEqual(earliest_ancestor(test_ancestors, 6), 10)
        self.assertEqual(earliest_ancestor(test_ancestors, 7), 4)  # not 11  hmmm, shortest path to futhest target v
        self.assertEqual(earliest_ancestor(test_ancestors, 8), 4)  # not 11
        self.assertEqual(earliest_ancestor(test_ancestors, 9), 4)  # not 11
        self.assertEqual(earliest_ancestor(test_ancestors, 10), -1)
        self.assertEqual(earliest_ancestor(test_ancestors, 11), -1)
"""

# 1) Translate problem into graph terminology
#   - earliest_ancestor >> first arg is array of tuples >> each tuple element is a vertex
#   - earliest_ancestor >> first arg is array of tuples >> each tuple pair is an edge
# !!!    -  First tuple element is PARENT, second tuple element is CHILD
# watch order ? of parents
# 2) Build your graph
#   - use first arg to generate adjacency list
#    
# 3) Traverse your graph
# traverse 'up' from child vertex to each immediate neighbor('parent') until no more parents to find

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (11, 8), (8, 9), (4, 8), (10, 1)]
earliest_ancestor(test_ancestors, 9)
graph.show_connected_vertices()
#   Vertex 1  has edge to vertice(s) : {3}
#   Vertex 3  has edge to vertice(s) : {6}
#   Vertex 2  has edge to vertice(s) : {3}
#   Vertex 5  has edge to vertice(s) : {6, 7}
#   Vertex 4  has edge to vertice(s) : {8, 5}
#   Vertex 8  has edge to vertice(s) : {9}
#   Vertex 11  has edge to vertice(s) : {8}
#   Vertex 10  has edge to vertice(s) : {1}