"""
1) Translate problem into graph terminology
    - Vertices are users
    - edges are undirected and are friendships
    - this is cyclic graph
2) Build your graph
3) Traverse your graph
    - use BFS 

"""


import random

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


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0   
        self.users = {}    # maps IDs to User obj   (works as lookup table)
        
        # Adjacency list (edge relationships to a vertex)
        self.friendships = {}  # maps user_IDs t0 list of other users(via friendships) 

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:   # !!!!!  THIS creates TWO-WAY relatiopnship (undirected)
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """

        # print(f'  name passed in is {name}')
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0   #### !!!!  NOTICE THIS !!!!!
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        #####   Add users
        # Loop through (use id to create name) 
        for i in range(num_users):
            self.add_user(f' User_{i}')

        #####   Create friendships
        #  generate all possible friendships
        # randomly select a set  X friendships so avg friendships is 2
        # we divide by because friendships are bidirectional
        possible_friendships = []
        
        # since relationship is bidrectional, inner for loop only runs n/2
        # n * (n/2) => (n^2)/2 => 0.5*(n^2) => n^2 => O(n^2)
        for user_id in self.users:
            # print(f' user_id: {user_id}  friend_id: {self.last_id} ')
            for friend_id in range(user_id + 1, self.last_id + 1):
                # print(f' friend_id  {friend_id}')
                possible_friendships.append( (user_id, friend_id) )


        # shuffle random_frienships and pick x elements from front
        random.shuffle(possible_friendships)
        num_friendships = (num_users * avg_friendships) // 2
        print(f' num_friendships {num_friendships} ')

        
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]   # tuple
            # print(f' \t bidirectional friendship {friendship}')
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """ 
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # BSD !!!
        q = Queue()
        q.enqueue([user_id])    
        
        while q.size() > 0:             # while queue not empty
            path = q.dequeue()          
            current_user = path[-1]

            if current_user not in visited:         # check if visited
                visited[current_user] = path
                # print(f' \t visited set is {visited} ')

                for friend in self.friendships[current_user]:   # check 'neighbors'
                    path_c = path[:]
                    path_c.append(friend)
                    q.enqueue(path_c)
                # print(f' \t\t NOW enqueued paths {q.queue}\n') 

        return visited

    def show_all_users(self):
        
        for k,v in self.users.items():
            print(f' k {k}: {v.name}')
   

if __name__ == '__main__':
    sg = SocialGraph()
    # sg.populate_graph(10, 2)   # num_friendships 10 
    # sg.populate_graph(50, 4)   # num_friendships 100
    # sg.populate_graph(50, 40)    # num_friendships 1000
    # sg.populate_graph(10, 4)      # num_friendships 20
    sg.populate_graph(1000, 4)    

    print(f' \t {sg.friendships} ')  # Will be DIFFERENT for each run
        #  num_friendships 5 
        #          bidrectional friendship (4, 5)
        #          bidrectional friendship (2, 4)
        #          bidrectional friendship (2, 3)
        #          bidrectional friendship (1, 3)
        #          bidrectional friendship (1, 2)
        # {1: {2, 3}, 2: {1, 3, 4}, 3: {1, 2}, 4: {2, 5}, 5: {4}}

    for k,v in sg.friendships.items():
        if len(v) == 0:
            print(f' k {k} is empty set')    

    # print(sg.show_all_users())

    # user with NO friendships yet  ex 3: set()   
    # ex {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}

    # connections = sg.get_all_social_paths(1)
    # print(connections)
    # {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}

    # print(sg.last_id)

    # for i in range(1,sg.last_id + 1):
    #     connections = sg.get_all_social_paths(i)
    #     print(f'\n bfs from {i} to >> {connections}')