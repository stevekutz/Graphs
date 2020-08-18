
# Note: This Queue class is sub-optimal. Why?, These use lists that append in O(1), but remove in O(n)
class Queue():   # FIFO   or LILO
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

class Stack():      # LIFO
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


# q = Queue()
# q.enqueue("A")
# q.enqueue("B")
# print(q.size())
# print(f' q is : {q.queue}')  # q is : ['A', 'B']
# q.dequeue()
# print(f' q is {q.queue}')    # q is ['B']      FIFO



# s = Stack()
# s.push("First")
# s.push("Next")
# s.push("Last")
# print(f' s is : {s.stack}')   # s is : ['First', 'Next', 'Last']
# print(s.size())    # 3
# s.pop()
# print(f' s is {s.stack}')    # s is ['First', 'Next']
# print(s.size())    # 2