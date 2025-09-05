# a. Add at head 
# b. Add at tail 
# c. Delete at head 
# d. Delete at tail 
# e. Add after given data 
# f. Delete after given data 
# g. Search an element 


class LinkedList:
    class _node_:
        def __init__(self, ele):
            self.data = ele
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def get_count(self):
        return self.count

    #add at head
    def add_at_head(self, ele):
        new_node = self._node_(ele)
        if not self.is_empty():
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1


    # add at tail
    def add_at_tail(self, ele):
        new_node = self._node_(ele)
        if not self.is_empty():
            self.tail.next = new_node
            self.tail =  new_node
        else:
            self.head = self.tail = new_node
        self.count += 1

    # delete at head
    def delete_at_head(self):
        if not self.is_empty():
            data = self.head.data
            cur = self.head
            self.head = cur.next
            cur.next = None
            self.count -= 1
            return data
        else:
            return None

    # delete at tail
    def delete_at_tail(self):
        if not self.is_empty():
            data = self.tail.data
            if self.count > 1:
                last = self.tail
                cur = self.head
                while cur.next != last:
                    cur = cur.next
                cur.next = None
                self.tail = cur
            else:
                self.head = self.tail = None
            self.count -= 1
            return data
        else:
            return None
                       

s = LinkedList()
s.add_at_head(2)
s.add_at_tail(3)
s.add_at_tail(4)
print(s.delete_at_head())
print(s.delete_at_head())