from a_single_linkedlist import *
from b_merge_two_common_LL import *
from c_sum_last_n_nodes import *
from d_reverse_LL import *
from e_split_LL import *
from f_palindrome_LL import *
from g_duplicates_rm import *
from h_middle_ele import *
from i_remove_odd_ele_circular_ll import *
from j_ll_contains_cycle import *


def test_empty_list():
    s1 = LinkedList()
    assert(s1.is_empty() == True)
    assert(s1.get_count() == 0)

# test_empty_list()

def test_adding_head():
    s2 = LinkedList()
    s2.add_at_head(3)
    assert(s2.get_count() == 1)

# test_adding_head()

def test_adding_tail():
    s3 = LinkedList()
    s3.add_at_tail(7)
    s3.add_at_tail(9)
    s3.add_at_tail(8)
    assert(s3.get_count() == 3)

# test_adding_tail()

def test_delete_at_head():
    s4 = LinkedList()
    s4.add_at_head(1)
    s4.add_at_head(2)
    s4.add_at_head(3)
    s4.delete_at_head()
    s4.delete_at_tail()
    assert(s4.get_count() == 2)

# test_delete_at_head()

def test_search_an_ele():
    s5 = LinkedList()
    s5.add_at_head(1)
    s5.add_at_head(2)
    s5.add_at_head(3)
    assert(s5.search_an_ele(2) == True)

# test_search_an_ele()

def test_add_after_data():
    s6 = LinkedList()
    s6.add_at_head(1)
    s6.add_at_head(2)
    s6.add_at_head(3)
    s6.add_after_data(3, 4)
    assert(s6.get_count() == 4)

# test_add_after_data()

def test_delete_after_data():
    s7 = LinkedList()
    s7.add_at_head(1)
    s7.add_after_data(1, 2)
    s7.add_after_data(2, 3)
    s7.add_after_data(3, 4)
    s7.display()

# test_delete_after_data()

def test_display():
    s8 = LinkedList()
    s8.add_at_head(1)
    s8.add_at_head(2)
    s8.add_at_head(3)
    s8.add_after_data(1, 4)
    s8.add_after_data(2, 4)
    s8.add_after_data(3, 4)
    s8.delete_after_data(4)
    s8.delete_at_head()
    s8.delete_at_tail()
    s8.add_at_tail(9)
    s8.delete_after_data(9)
    print(s8.search_an_ele(9))
    print(s8.is_empty())
    print(s8.get_count())
    s8.display()

# test_display()

#------------------------------ a_single_linkedlist testing ends here -------------------------------------------------

def test_get_common_ele(): # 
    l1 = LinkedList()
    l1.add_at_tail(1)
    l1.add_at_tail(2)
    l1.add_at_tail(3)
    l1.add_at_tail(4)

    l2 = LinkedList()
    l2.add_at_tail(3)
    l2.add_at_tail(4)
    l2.add_at_tail(5)
    l2.add_at_tail(6)

    common = get_common_ele(l1, l2)
    l1.display()
    l2.display()
    common.display()

# test_get_common_ele()

#--------------------------------- b_merge_two_common_LL testing ends here ------------------------------------------------

def test_sum_of_ele():
    l1 = LinkedList()
    l1.add_at_tail(1)
    l1.add_at_tail(3)
    l1.add_at_tail(3)
    l1.add_at_tail(4)
    l1.add_at_tail(5)

    s = sum_of_ele(l1)

    print(s)

# test_sum_of_ele()

#---------------------------------- c_sum_last_n_nodes testing ends here ----------------------------------------------------

def test_rev_ll():
    l1 = LinkedList()
    l1.add_at_tail(1)
    l1.add_at_tail(2)
    l1.add_at_tail(3)
    l1.add_at_tail(4)

    l1.display()
    reverse_linkedlist(l1)
    l1.display()

# test_rev_ll()

#---------------------------------- d_reverse_LL testing ends here ------------------------------------------------------------

def test_linkedlist_split():
    l1 = LinkedList()
    l1.add_at_tail(1)
    l1.add_at_tail(2)
    l1.add_at_tail(3)
    l1.add_at_tail(4)
    l1.add_at_tail(5)
    l1.add_at_tail(6)

    linkedlist_split(l1)

# test_linkedlist_split()

#----------------------------------- e_split_LL testing ends here --------------------------------------------------------------

def test_palindrome_LL():
    l1 = LinkedList()
    l1.add_at_tail(1)
    l1.add_at_tail(2)
    l1.add_at_tail(3)
    l1.add_at_tail(7)
    l1.add_at_tail(2)
    l1.add_at_tail(1)
    print(palindrome_LL(l1))

# test_palindrome_LL()

#------------------------------------ f_palindrome_LL testing ends here ---------------------------------------------------------

def test_remove_duplicates():
    l1 = LinkedList()
    l1.add_at_tail(1)
    l1.add_at_tail(2)
    l1.add_at_tail(3)
    l1.add_at_tail(0)
    l1.add_at_tail(2)
    l1.add_at_tail(1)
    print(remove_duplicates(l1))

# test_remove_duplicates() 

#------------------------------------ g_duplicates_rm testing ends here ----------------------------------------------------------

def test_middle_ele():
    l1 = LinkedList()
    l1.add_at_tail(2)
    l1.add_at_tail(3)
    l1.add_at_tail(4)
    l1.add_at_tail(5)
    print(middle_ele(l1))

# test_middle_ele()

#------------------------------------- h_middle_ele testing ends here -------------------------------------------------------------

def test_remove_odd_ele():
    cll = CircularLinkedList()

    n1 = CircularLinkedList._Node(10)
    n2 = CircularLinkedList._Node(21)
    n3 = CircularLinkedList._Node(34)
    n4 = CircularLinkedList._Node(43)
    n5 = CircularLinkedList._Node(50)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n1

    cll.head = n1
    cll.tail = n5
    cll.count = 5

    print("Original list:")
    cll.display()

    cll.remove_odd_elements()

    print("\nAfter removing odd elements:")
    cll.display()

# test_remove_odd_ele()

#----------------------------------------- i_remove_odd_ele_circular_ll testing ends here -----------------------------------------
def test_ll_contains_cycle():
    l1 = LinkedList()
    l1.add_at_tail(2)
    l1.add_at_tail(3)
    l1.add_at_tail(4)
    l1.add_at_tail(5)
    print(ll_contains_cycle(l1))

    cll = CircularLinkedList()
    
    n1 = CircularLinkedList._Node(10)
    n2 = CircularLinkedList._Node(21)
    n3 = CircularLinkedList._Node(34)
    n4 = CircularLinkedList._Node(43)
    n5 = CircularLinkedList._Node(50)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n1
    
    cll.head = n1
    cll.tail = n5
    cll.count = 5
    
    print(ll_contains_cycle(cll))


# test_ll_contains_cycle()

#-------------------------------------------- j_ll_contains_cycle testing ends here ----------------------------------------