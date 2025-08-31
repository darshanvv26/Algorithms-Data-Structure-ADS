class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def peek(self):
        return None if self.is_empty() else self.data[0]

    def display(self):
        print("Queue (front -> rear):", self.data)

    def rotate(self):
        if self.is_empty():
            print("Queue is empty, nothing to rotate")
            return

        self.data = self.data[::-1]
        print("Queue after rotation (reversed):", self.data)

Q = Queue()
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)

Q.display()

Q.rotate()  
Q.display()
