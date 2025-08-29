class Stack:

    def __init__(self):
        self.data = []
    
    def push(self, ele):
        self.data.append(ele)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return None
    
    def is_empty(self):
        return len(self.data) == 0
    
def reverse_file(inp_file, out_file):
    s = Stack()

    with open(inp_file, 'r') as f:
        for line in f:
            s.push(line.rstrip('\n'))

    with open(out_file, 'w') as f:
        while not s.is_empty():
            f.write(s.pop() + '\n')


inp_file = 'input.txt'
out_file = 'reversed_output.txt'
reverse_file(inp_file, out_file)
print(f"File reversed and saved to {out_file}")