from a_single_linkedlist import *


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
    assert(s3.get_count() == 1)

test_adding_tail()