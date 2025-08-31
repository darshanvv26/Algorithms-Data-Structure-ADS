class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)   

    def dequeue(self):
        if self.is_empty():
            return None
        return self.data.pop(0)  

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def front(self):
        if self.is_empty():
            return None
        return self.data[0]

# ---------------------------------------------------------------- #

class StackUsingQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        print(f"Pushing {x}")
        self.q2.enqueue(x)

        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1.is_empty():
            print("Stack is empty, nothing to pop")
            return None
        removed = self.q1.dequeue()
        print(f"Popped {removed}")
        return removed

    def peek(self):
        return self.q1.front()

    def is_empty(self):
        return self.q1.is_empty()

    def size(self):
        return self.q1.size()

    def display(self):
        print("Stack (top -> bottom):", self.q1.data)

S = StackUsingQueues()

S.push(10)
S.push(20)
S.push(30)
S.display()

print("Top element is:", S.peek())
S.pop()
S.display()
S.pop()
S.display()

print("Is stack empty?", S.is_empty())