class stack:
    def __init__(self):
        self.data = []

    def push(self, ele):
        self.data.append(ele)

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
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)
    
    def display(self):
        return self.data

s = stack()
while 1:
    print("\n\nAction needs to be performed\n 1. push\n 2. pop\n 3. peek\n 4. exit\n 5. size of stack\n 6. display")
    inp = int(input("Select the action: "))
    if inp == 1:
        ele = input("Enter the ele that needs to be pushed: ")
        s.push(ele)
    elif inp == 2:
        print("The popped ele is: ", s.pop())
    elif inp == 3:
        print("The top element is: ", s.peek())
    elif inp == 4:
        exit()
    elif inp == 5:
        print("The size of stack is: ", s.size())
    elif inp == 6:
        print(s.display())