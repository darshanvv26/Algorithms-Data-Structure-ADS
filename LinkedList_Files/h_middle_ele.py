from a_single_linkedlist import *

def middle_ele(list1):
    # len_ll = list1.get_count()
    # middle_len = (len_ll // 2)
    # cur = list1.head

    # for _ in range(middle_len):
    #     cur = cur.next
    # return cur.data
    
    one_skip = list1.head
    two_skip = list1.head

    while two_skip and two_skip.next:
        one_skip = one_skip.next
        two_skip = two_skip.next.next

    return one_skip.data if one_skip else None

# l1 = LinkedList()
# l1.add_at_tail(None)
# l1.add_at_tail(2)
# l1.add_at_tail(3)
# l1.add_at_tail(4)
# l1.add_at_tail(5)
# print(middle_ele(l1))