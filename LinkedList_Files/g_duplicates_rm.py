from a_single_linkedlist import *

def remove_duplicates(list1):
    set1 = set()

    cur = list1.head

    while cur:
        set1.add(cur.data)
        cur = cur.next
            

l1 = LinkedList()
l1.add_at_tail(1)
l1.add_at_tail(2)
l1.add_at_tail(3)
l1.add_at_tail(0)
l1.add_at_tail(2)
l1.add_at_tail(1)

print(remove_duplicates(l1)) 