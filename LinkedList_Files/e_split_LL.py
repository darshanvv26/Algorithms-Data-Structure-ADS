from a_single_linkedlist import *

def linkedlist_split(original_list):
    list1 = LinkedList()
    list2 = LinkedList()

    toggle = True

    cur = original_list.head

    while cur != None:
        if toggle:
            list1.add_at_tail(cur.data)
        else:
            list2.add_at_tail(cur.data)
        cur = cur.next
        toggle = not toggle

    return list1.display(), list2.display()

# l1 = LinkedList()
# l1.add_at_tail(1)
# l1.add_at_tail(2)
# l1.add_at_tail(3)
# l1.add_at_tail(4)
# l1.add_at_tail(5)
# l1.add_at_tail(6)

# linkedlist_split(l1)