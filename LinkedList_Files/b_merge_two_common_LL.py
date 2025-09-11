from a_single_linkedlist import *

def get_common_ele(list1, list2):
    LL = LinkedList()
    set1 = set()

    cur1 = list1.head
    while cur1 != None:
        set1.add(cur1.data)
        cur1 = cur1.next

    cur2 = list2.head
    while cur2 != None:
        if cur2.data in set1:
            LL.add_at_tail(cur2.data)
        cur2 = cur2.next
    
    return LL

# l1 = LinkedList()
# l1.add_at_tail(1)
# l1.add_at_tail(2)
# l1.add_at_tail(3)
# l1.add_at_tail(4)

# l2 = LinkedList()
# l2.add_at_tail(3)
# l2.add_at_tail(4)
# l2.add_at_tail(5)
# l2.add_at_tail(6)

# common = get_common_ele(l1, l2)

# common.display()