from a_single_linkedlist import *

def palindrome_LL(list1):
    lst = []
    cur = list1.head

    while cur:
        lst.append(cur.data)
        cur = cur.next

    return lst == lst[::-1]

# l1 = LinkedList()
# l1.add_at_tail(1)
# l1.add_at_tail(2)
# l1.add_at_tail(3)
# l1.add_at_tail(3)
# l1.add_at_tail(2)
# l1.add_at_tail(1)

# print(palindrome_LL(l1))