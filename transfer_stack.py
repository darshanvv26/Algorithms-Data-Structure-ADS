def transfer(S, T):
    temp = []

    while S:
        temp.append(S.pop())

    while temp:
        T.append(temp.pop())

S = [1, 2, 3, 4] 
T = []

transfer(S, T)

print("S:", S)  
print("T:", T)