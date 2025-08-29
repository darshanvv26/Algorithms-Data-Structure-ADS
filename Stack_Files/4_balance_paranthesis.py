class Match:

    def __init__(self):
        self.data = []

    def balance(self, str_inp):
        mapper = {'(' : ')', '{' : '}', '[' : ']'}

        for i in str_inp:
            if i in mapper:
                self.data.append(i)

            else:
                if not self.data:
                    print("Invalid Match!!!")
                    return

                top = self.data.pop()
                
                if mapper[top] != i:
                    print("Invalid Match!!!")
                    return
                
        if self.data:
            print("Invalid Match!!!")
        else:
            print("Valid Match")

m = Match()
inp = input("Enter the string input: ")
m.balance(inp)