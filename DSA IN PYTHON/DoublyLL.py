class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        current = self.head
        while current is not None and current.data != data:
            current = current.next

        if current is not None:
            if current.prev is not None:
                current.prev.next = current.next
            else:
                self.head = current.next

            if current.next is not None:
                current.next.prev = current.prev
            else:
                self.tail = current.prev

    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def display_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
        print(" -> ".join(map(str, elements)))

# Example usage:
my_doubly_linked_list = DoublyLinkedList()
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.prepend(0)

my_doubly_linked_list.display_forward()  # Output: 0 -> 1 -> 2 -> 3
my_doubly_linked_list.display_backward()  # Output: 3 -> 2 -> 1 -> 0

my_doubly_linked_list.delete(2)
my_doubly_linked_list.display_forward()  # Output: 0 -> 1 -> 3
my_doubly_linked_list.display_backward()  # Output: 3 -> 1 -> 0
