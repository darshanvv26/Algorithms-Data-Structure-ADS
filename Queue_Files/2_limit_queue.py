class LimitQueue:

    def __init__(self, max_capacity):
        self.data = []
        self.max_capacity = max_capacity

    def enqueue(self, ele):
        if self.size() < self.max_capacity:
            self.data.append(ele)
        else:
            print("The queue is full")
            return
        
    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        else:
            print("The queue is empty there is nothing to dequeue")
            return
        
    def peek(self):
        if not self.is_empty():
            return self.data[0]
        else:
            return None
        
    def is_empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)
    
max_size = int(input("Enter the size of the queue: "))
LQ = LimitQueue(max_size)

LQ.enqueue(10)
LQ.enqueue(20)
LQ.enqueue(30)
LQ.enqueue(40)
LQ.enqueue(50)
LQ.enqueue(60)
LQ.enqueue(70)
LQ.enqueue(80)
LQ.enqueue(90)

print("The dequeued element is: ", LQ.dequeue())
print("The dequeued element is: ", LQ.dequeue())
print("The dequeued element is: ", LQ.dequeue())
print("The dequeued element is: ", LQ.dequeue())
print("The dequeued element is: ", LQ.dequeue())
print("The dequeued element is: ", LQ.dequeue())
print("The dequeued element is: ", LQ.dequeue())
print("The dequeued element is: ", LQ.dequeue())
print("The dequeued element is: ", LQ.dequeue())

print("The front element is: ", LQ.peek())
print("Is the queue empty? ", LQ.is_empty())
print("What is the size of the queue? ", LQ.size())