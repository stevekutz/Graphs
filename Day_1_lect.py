#  Doing Follow Along before looking at solution

# Adjacency List
class Graph:    
    def __init__(self):
        self.verticies = {
            # "V": {set of neighbor V's: weight of Edge} to get to V
            # "A": {'B'},  # need to include weight
            
            "A": {'B': 1},
            "B": {'C': 3, 'D': 2},
            "C": {}, # no neighbors
            "D": {},
            "E": {'D': 1},
        }


# Adjancency Matrix
class Graph:
    def __init__(self):
        self.edges = [
           # A B C D E
        #A  [0, 1, 0, 0, 0 ],
        #B  [0, 0, 3, 2, 0],
        #C  [0, 0, 0, 0, 0],
        #D  [0, 0, 0, 0, 0],
        #E  [0, 0, 0, 1, 0]
        ]   


# Challenge
class Graph:
    def __init__(self):
        self.verticies = {
            "A": {'B': 1},
            "B": {'C': 3, 'E': 1, 'D': 2},
            "C": {'E': 4},
            "D": {'E': 2},
            "E": {'F': 2},
            "F": {},
            "G": {'D': 1}
        }              

class Graph:
    def __init__(self):
        self.vertices = [
      #  A  B  C  D  E  F  G     
    #A  [0, 1, 0, 0, 0, 0, 0],
    #B  [0, 0, 3, 2, 1, 0, 0],
    #C  [0, 0, 0, 0, 4, 0, 0],
    #D  [0, 0, 0, 0, 2, 0, 0],
    #E  [0, 0, 0, 0, 0, 3, 0],
    #F  [0, 0, 0, 0, 0, 0, 0],
    #G  [0, 0, 0, 1, 0, 0, 0],
        ]        