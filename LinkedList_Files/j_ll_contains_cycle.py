from a_single_linkedlist import *
from i_remove_odd_ele_circular_ll import *

def ll_contains_cycle(list1):

    slow = list1.head
    fast = list1.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return "linked list contains cycle"
        
    return "linked list does not contain cycle"

# l1 = LinkedList()
# l1.add_at_tail(2)
# l1.add_at_tail(3)
# l1.add_at_tail(4)
# l1.add_at_tail(5)
# print(ll_contains_cycle(l1))

# cll = CircularLinkedList()

# n1 = CircularLinkedList._Node(10)
# n2 = CircularLinkedList._Node(21)
# n3 = CircularLinkedList._Node(34)
# n4 = CircularLinkedList._Node(43)
# n5 = CircularLinkedList._Node(50)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n1

# cll.head = n1
# cll.tail = n5
# cll.count = 5

# print(ll_contains_cycle(cll))