class FlexiQueue:

    def __init__(self, initial_capacity=2):
        self.data = [None] * initial_capacity  
        self.capacity = initial_capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, ele):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = ele
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty, nothing to dequeue")
            return None
        removed = self.data[self.front]
        self.data[self.front] = None 
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if 0 < self.size <= self.capacity // 4:
            self._resize(self.capacity // 2)
        return removed

    def peek(self):
        return None if self.is_empty() else self.data[self.front]

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[(self.front + i) % self.capacity]
        self.data = new_data
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.size - 1

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            elements = [self.data[(self.front + i) % self.capacity] for i in range(self.size)]
            print("Queue:", elements, "| Capacity:", self.capacity, "| Size:", self.size)

FQ = FlexiQueue()

# Perform enqueues
FQ.enqueue(10)
FQ.enqueue(20)
FQ.enqueue(30)  # should expand here
FQ.enqueue(40)
FQ.enqueue(50)

# Perform dequeues
FQ.dequeue()
FQ.dequeue()
FQ.dequeue()    # may shrink here

# Peek
print("Front element is:", FQ.peek())

# Check if empty
print("Is queue empty?", FQ.is_empty())

# Final state
FQ.display()