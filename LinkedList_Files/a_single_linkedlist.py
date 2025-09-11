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
        
    # Add after given data 
    def add_after_data(self, key, ele):
        new_node = self._node_(ele)
        cur = self.head
        while cur != None:
            if cur.data == key:
                new_node.next = cur.next
                cur.next = new_node
                if cur == self.tail:
                    self.tail = new_node
                self.count += 1
                return   
            else:
                cur = cur.next
        return "Key not found"
                
    # Delete after given data
    def delete_after_data(self, key):
        cur = self.head
        while cur != None:
            if cur.data == key:
                temp = cur.next
                removed_count = 0
                while temp != None:
                    removed_count += 1
                    temp = temp.next

                cur.next = None
                self.tail = cur
                self.count -= removed_count
                return  
            else:
                cur = cur.next
        return "Key not found"

            
    # Search an element
    def search_an_ele(self, key):
        cur = self.head
        while cur != None:
            if cur.data == key:
                break
            else:
                cur = cur.next
        return cur != None      

    # Display linkedlist
    def display(self):
        cur = self.head
        while cur != None:
            print(f"[{cur.data}]", end='->')
            cur = cur.next
        print(None)
        if not self.is_empty():
            print("Head of the linked list is ", self.head.data)
            print("Tail of the linked list is", self.tail.data)
        else:
            print("List is empty")