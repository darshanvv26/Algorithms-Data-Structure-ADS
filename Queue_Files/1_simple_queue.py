class SimpleQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, ele):
        self.queue.append(ele)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty no element to dequeue")
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            print("Queue is empty no element to peak")
            return 
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    

q = SimpleQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front item:", q.peek())    
print("Dequeued:", q.dequeue())   
print("Dequeued:", q.dequeue())   

print("Queue size:", q.size())    
print("Is queue empty?", q.is_empty())  