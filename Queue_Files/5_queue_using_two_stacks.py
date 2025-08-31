class QueueUsingStacks:
    def __init__(self):
        self.s1 = []  
        self.s2 = []  

    def enqueue(self, x):
        print(f"Enqueue: {x}")
        self.s1.append(x)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, nothing to dequeue")
            return None

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        removed = self.s2.pop()
        print(f"Dequeued: {removed}")
        return removed

    def peek(self):
        if self.is_empty():
            return None
    
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def is_empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0

    def size(self):
        return len(self.s1) + len(self.s2)

    def display(self):
        
        temp = self.s2[::-1] + self.s1
        print("Queue (front -> rear):", temp)

Q = QueueUsingStacks()

Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.display()

print("Front element is:", Q.peek())
Q.dequeue()
Q.display()
Q.dequeue()
Q.display()

print("Is queue empty?", Q.is_empty())
