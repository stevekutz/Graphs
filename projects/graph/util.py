
# Note: This Queue class is sub-optimal. Why?, These use lists that append in O(1), but remove in O(n)
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

class Stack():      # LIFO
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)        # REMEBER periodic resizing
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()     # this is O(n)
        else:
            return None
    def size(self):
        return len(self.stack)


# q = Queue()
# q.enqueue("A")   # add "A" to end of queue, "like lining up to pay at store"
# q.enqueue("B")   # add " B" to end of queue, "get in end of line"
# print(q.size())  # 2
# print(f' q is : {q.queue}')  # q is : ['A', 'B']
# q.dequeue()    # FIFO, remove FIRST from queue and return it
# print(f' q is {q.queue}')    # q is ['B']      FIFO



# s = Stack()
# s.push("First")   # append to end of Stack
# s.push("Next")
# s.push("Last")
# print(f' s is : {s.stack}')   # s is : ['First', 'Next', 'Last']
# print(s.size())    # 3
# s.pop()        # LIFO, remove last one added(ex. pushed) from Stack and return it
# print(f' s is {s.stack}')    # s is ['First', 'Next']
# print(s.size())    # 2