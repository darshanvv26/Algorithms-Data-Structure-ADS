from a_single_linkedlist import *

def reverse_linkedlist(list1):

    prev = None
    cur = list1.head
    list1.tail = list1.head 

    while cur != None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    
    list1.head = prev
        
    return list1  

# l1 = LinkedList()
# l1.add_at_tail(1)
# l1.add_at_tail(2)
# l1.add_at_tail(3)
# l1.add_at_tail(4)

# l1.display()
# reverse_linkedlist(l1)
# l1.display()