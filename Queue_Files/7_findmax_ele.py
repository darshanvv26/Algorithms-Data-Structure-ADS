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

    def findMax(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        max_val = float('-inf')
        n = self.size()

        for i in range(n):
            ele = self.dequeue()      
            if ele > max_val:         
                max_val = ele
            self.enqueue(ele)         

        print("Maximum element in queue is:", max_val)
        return max_val

Q = Queue()
Q.enqueue(10)
Q.enqueue(40)
Q.enqueue(25)
Q.enqueue(5)

Q.display()

Q.findMax()   

Q.display()  
