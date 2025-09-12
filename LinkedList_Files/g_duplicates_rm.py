from a_single_linkedlist import *

def remove_duplicates(list1):

    if not list1.head:
        return None
    
    set1 = set()
    cur = list1.head
    set1.add(cur.data)

    while cur.next:
        if cur.next.data in set1:
            cur.next = cur.next.next
        else:
            set1.add(cur.next.data)
            cur = cur.next
    
    list1.tail = cur
    return list1.display()    

# l1 = LinkedList()
# l1.add_at_tail(1)
# l1.add_at_tail(2)
# l1.add_at_tail(3)
# l1.add_at_tail(0)
# l1.add_at_tail(2)
# l1.add_at_tail(1)

# print(remove_duplicates(l1)) 