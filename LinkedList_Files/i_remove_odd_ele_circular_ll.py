class CircularLinkedList:
    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def display(self):
        if self.is_empty():
            print("List is empty")
            return

        result = []
        cur = self.head
        while True:
            result.append(f"[{cur.data}]")
            cur = cur.next
            if cur == self.head:
                break
        print(" -> ".join(result))
        print("Head:", self.head.data)
        print("Tail:", self.tail.data)

    def remove_odd_elements(self):
        if self.is_empty():
            return

        cur = self.head
        prev = self.tail  
        removed_count = 0

        while True:
            next_node = cur.next
            if cur.data % 2 != 0:
                if cur == self.head:
                    self.head = next_node
                    self.tail.next = self.head
                if cur == self.tail:
                    self.tail = prev
                    self.tail.next = self.head

                prev.next = next_node
                self.count -= 1
                removed_count += 1

                if self.head == self.tail and self.head.data % 2 != 0:
                    self.head = None
                    self.tail = None
                    self.count = 0
                    return
                cur = next_node
            else:
                prev = cur
                cur = next_node

            if cur == self.head:
                break


# cll = CircularLinkedList()

# n1 = CircularLinkedList._Node(10)
# n2 = CircularLinkedList._Node(21)
# n3 = CircularLinkedList._Node(34)
# n4 = CircularLinkedList._Node(43)
# n5 = CircularLinkedList._Node(50)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n1

# cll.head = n1
# cll.tail = n5
# cll.count = 5

# print("Original list:")
# cll.display()

# cll.remove_odd_elements()

# print("\nAfter removing odd elements:")
# cll.display()
