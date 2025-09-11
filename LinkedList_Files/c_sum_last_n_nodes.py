from a_single_linkedlist import *

def sum_of_ele(list1):
    i = j = list1.head

    n = int(input("Enter the n value: "))

    if n <= 0:
        return 0
    
    for _ in range(n):
        if j == None:
            return "n value is greater than the size of the linked list"
        j = j.next

    while j != None:
        i = i.next
        j = j.next

    summ = 0

    while i != None:
        summ += i.data
        i = i.next

    return summ 

# l1 = LinkedList()
# l1.add_at_tail(1)
# l1.add_at_tail(3)
# l1.add_at_tail(3)
# l1.add_at_tail(4)
# l1.add_at_tail(5)

# s = sum_of_ele(l1)

# print(s)