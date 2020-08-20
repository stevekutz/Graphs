"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

# we are build an adjacency list
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

        ####   not quite
        # try:
        #     if v1 in self.vertices or v2 in self.vertices:
        #         self.vertices[v1].add(v2)
        # except:
        #     raise ValueError(" BAD VERTEX !!")


        if v1 not in self.vertices or v2 not in self.vertices:
            raise ValueError(" BAD VERTEX !!")
        else:
            self.vertices[v1].add(v2)


    def add_undirected_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)    

        

    def show_connected(self):
        print(f' Immediate neighbors')
        for item in self.vertices:
            for set_item in self.vertices[item]:
                # print(f'  dict {item}  contains set items: {self.vertices[item]}')
                print(f'  Vertex {item}  has edge to vertice(s) : {self.vertices[item]}')
                break


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO
        if vertex_id in self.vertices:
            # print(f' self.vertices[vertex_id] >> {self.vertices[vertex_id]} ')
            return self.vertices[vertex_id]
        else:
            # print(f' ERROR:  vertex {vertex.id} does not exist')    
            raise ValueError("get_neighbor cannot locate vertex {vertex_id}")


    # this is a traversal, NOT SEARCH            
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        """      FIFO   is LILO
        Create a queue
        Enqueue starting Vertex
        Create a set top store visited
        
        While the queue is NOT empty:  e.g.   > 0
            Dequeue the first Vertex
            Check IF NOT visited:
                Mark as visited
                enqueue ALL  neighbors  found if not already in queue
        """
                # FIFO     
        q = Queue()                      # create a queue  ( e.g. empty []  )
        q.enqueue(starting_vertex)       # Enqeue starting at vertex
        visited = set()                  # Create a set to store visited

        print(f' SIZE: {q.size()} ')
        while q.size() > 0:              # While the queue is NOT empty:
        # while q:             # ERROR: Will add  None  into v, breaks _get_neighbors
            v = q.dequeue()                  # dequeue the first vertex
            print(f' \n\t dequeue v is : {v}')
            print(f' \t size: {q.size()} ')
            if v not in visited:         # Check IF NOT visited:   
                print(v)
                visited.add(v)           # if NOT visited, add to visited set
                print(f' \t visited set is {visited} ')  
                # print(f' \t v is:  {v}')         # if NOT visited, add to visited set

                for n in self.get_neighbors(v):    # loop through all neighbors of  v 
                    # if n not in q.queue:     # !!!  OPTIMIZATION !!!
                    #     q.enqueue(n)   # enqueue ALL neighbors found (ex. add to end of queue)

                    q.enqueue(n)   # enqueue ALL neighbors found (ex. add to end of queue)

                print(f' \t\t NOW enqueued {q.queue}')
            # print(f' v is {v} ')
            #return visited

            # pass  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        """       LIFO
        Create a stack  
        Push starting Vertex
        Create a set to store visited
        While the stack is NOT empty:    e.g.   > 0
            Pop the last added Vertex
                Check IF NOT visited:
                    Mark as visited


                Push ALL of neighbors
        """
        s = Stack()              # Create a stack
        s.push(starting_vertex)  # Push starting Vertex
        visited = set()          # Create a set to store visited

        print(f' SIZE: {s.size()} ')
        while s.size() > 0:        #  While the stack is NOT empty:    e.g.   > 0
            v = s.pop()                 # Pop the last added Vertex
            print(f' \n\t popped v is : {v}')
            print(f' \t size: {s.size()} ')

            if v not in visited:        # Check IF NOT visited:    e.g.   > 0
                print(v)
                visited.add(v)          # Mark as visited
                print(f' \t visited set is {visited} ') 
                for n in self.get_neighbors(v):   # Check IF NOT visited:
                    s.push(n)                    # Push ALL of neighbors   

                print(f'\t\t NOW PUSHED {s.stack}')
        # return visited


    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        """
        Check if Vertex is in visited
            if NOT visited, add to visited set
            Call dft_recursive on every neighbor    
            

        """
        # 1) base case >> where to stop recursion
        # 2) calls itself from within
        # 3) each iteration approaches base case

        # 1) base case >> where to stop recursion

        # init a set that persists after recursions loops to save visited
        if visited == None:
            visited = set()

        if starting_vertex not in visited:      # 1) & 3) Check if vertex has NOT been visited
            visited.add(starting_vertex)            #  if True, add to visited set
            print(f' \t visited set is {visited} ') 

            print(starting_vertex)

            # perform recursion on neighbor
            for n in self.get_neighbors(starting_vertex):
                print(f'\t vertex {starting_vertex} with neighbor(s) {self.get_neighbors(starting_vertex)} at neighbor {n}')
                self.dft_recursive(n, visited)         # 2) 

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.    
                !!!!!   ALWAYS PROVIDES shortest path because it goes by Vertex proximity(immediate adj, next adj, .. etc.)
        """
        """      FIFO   ir LILO
        Create a queue
        Enqueue PATH to starting Vertex
        Create a set top store visited vertices
        While the queue is NOT empty:  e.g.   > 0
            Dequeue the first PATH Vertex
            Get Vertex from END of PATH
            Check IF NOT visited:
                Mark as visited
                check if vertex is destination_vertex
                    If TRUE, return path
                enqueue PATH to ALL of neighbors   
                make COPY of current path
                add neighbor to path copy
                enqueue copy                
        """

        q = Queue()                         # Create a queue
        q.enqueue([starting_vertex])            # Enqueue starting at vertex into Queue (list)
        visited = set()                         # Create a set to store visited 
        print(f' SIZE: {q.size()} ') 
        while q.size() > 0:                     # While the queue is NOT empty: 
            print(f' \n\t Queue is {q.queue} with size: {q.size()}')
            path = q.dequeue()                      # Dequeue the first PATH Vertices
            print(f' \t Dequeued path: {path} with Queue size {q.size()}')
            v = path[-1]                            # Get Vertex from END of PATH
            print(f' \t Last v is {v} from vertex path: {path} ')
            if v not in visited:                    # Check IF NOT visited:
                visited.add(v)                          # Mark as visited
                print(f' \t visited set is {visited} ')
                if v == destination_vertex:             # check if vertex is destination_vertex
                    return path                             # If TRUE, return path, DONE

                for n in self.get_neighbors(v):         # enqueue PATH to ALL of neighbors
                    path_c = path [:]                       # make COPY of current path
                    path_c.append(n)                        # add neighbor to path copy
                    q.enqueue(path_c)                       # enqueue copy
                print(f' \t\t NOW enqueued paths {q.queue}')    

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        """       LIFO
        Create a stack
        Create a set to store visited
        PUSH starting vertex into an array (STACK)
        While the STACK is NOT empty    
            get((pop) first PATH vertex
            get Vertex from END of PATH
            check if NOT visited
                mark as visited
                check if vertex is destination_vertex
                    If TRUE, return path   
                PUSH path to ALL of neighbors
                    make copy of current path
                    add neighbor to path copy
                    PUSH path copy
        """   
        s = Stack()                             # Create a stack
        s.push([starting_vertex])                 # PUSH starting vertex into an array (STACK)
        visited = set()                         # Create a set to store visited
        print(f' SIZE: {s.size()} ')

        while s.size() > 0:                     # While the STACK is NOT empty
            print(f' \n\t Stack is {s.stack} with size: {s.size()}')
            path = s.pop()                          # get(pop) first PATH vertex
            print(f' \t Popped path: {path} with Queue size {s.size()}')
            v = path[-1]                            # get Vertex from END of PATH   
            print(f' \t Last v is {v} from vertex path: {path} ') 
            while v not in visited:                 # check if NOT visited
                visited.add(v)                      # mark as visited
                print(f' \t visited set is {visited} ')
                if v == destination_vertex:         # check if vertex is destination_vertex
                    return path                         # If TRUE, return path 

                for n in self.get_neighbors(v):     # PUSH path to ALL of neighbors
                    path_c = path[:]                # make copy of current path
                    #  path_c.extend([n])                # add neighbor to path copy
                    path_c.append(n)                     # add neighbor to path copy
                    s.push(path_c)                  # PUSH path copy

            print(f' \t\t NOW PUSHED paths {s.stack}')

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # 1) base case >> where to stop recursion
        # 2) calls itself from within
        # 3) each iteration approaches base case

        # init a set that persists after recursions loops to save visited set & path list
        if visited == None:
            visited = set()

        if path == None:
            path = []

        if starting_vertex not in visited:      # 1) & 3) Check if vertex has NOT been visited
            visited.add(starting_vertex)            #  if True, add to visited set
            path_c = path[:]    # copy path
            path_c.append(starting_vertex)

            print(f' path is now {path_c}')
            if starting_vertex == destination_vertex:         # check if vertex is destination_vertex
                    return path_c                         # If TRUE, return copied path 

            # perform recursion on neighbor
            for n in self.get_neighbors(starting_vertex):
                print(f'\t vertex {starting_vertex} with neighbor(s) {self.get_neighbors(starting_vertex)} at neighbor {n}')
                new_path = self.dfs_recursive(n, destination_vertex, visited, path_c)         # 2

                if new_path is not None:
                    return new_path

        return None        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)   # {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # graph.show_connected()
    #     #  Immediate neighbors
    #     #   Vertex 1  had edge to vertice(s) : {2}
    #     #   Vertex 2  had edge to vertice(s) : {3, 4}
    #     #   Vertex 3  had edge to vertice(s) : {5}
    #     #   Vertex 4  had edge to vertice(s) : {6, 7}
    #     #   Vertex 5  had edge to vertice(s) : {3}
    #     #   Vertex 6  had edge to vertice(s) : {3}
    #     #   Vertex 7  had edge to vertice(s) : {1, 6}

    # print(graph.get_neighbors(1))   # {2}
    # print(graph.get_neighbors(4))   # {6,7}

    # should raise Error
    # graph.add_edge(1, 200)

    # graph.bft(1)
    # print(f' bft   {graph.bft(1)} ')   # {1, 2, 3, 4, 5, 6, 7}
    # print(f' dft   {graph.dft(1)} ')   # {1, 2, 3, 4, 5, 6, 7}

    # print(f' bft   {graph.bft(2)} ')   # {1, 2, 3, 4, 5, 6, 7}
    # print(f' dft   {graph.dft(2)} ')   # {1, 2, 3, 4, 5, 6, 7}

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7    
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
