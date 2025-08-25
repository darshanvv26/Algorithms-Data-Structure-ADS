class LimitedSizeStack:
    
    def __init__(self, max_capacity):
        self.data = []
        self.max_capacity = max_capacity

    def push(self, ele):
        if self.size() < self.max_capacity:
            self.data.append(ele)
        else:
            return "Stack is full"
        
    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return "Stack is empty"
        
    def size(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def display(self):
        return self.data
    
# ----------------------------------------------------------------------------------------------------------------------------------------
    
max_size = int(input("Enter the max size of stack: "))
s = LimitedSizeStack(max_size)

while 1:
    inp = int(input("\n 1. Push\n 2. Pop\n 3. Peek\n 4. Size\n 5. Display\n 6. Check_is_empty\n 7. Any other key exit\n Select actions: "))

    if inp == 1:    
        ele = int(input("\nEnter the ele to be pushed: "))
        print(s.push(ele))

    elif inp == 2:
        print("\nThe poped ele is: ", s.pop())

    elif inp == 3:
        print("\nThe top ele of the stack is: ", s.peek())

    elif inp == 4:
        print("\nThe size of stack is: ", s.size())

    elif inp == 5:
        print("\nThe stack elements are: ", s.display())
    
    elif inp == 6:
        print("\nIs stack empty: ", s.is_empty())

    else:
        exit()