class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            current = self.head
            while current.next != self.head:
                current = current.next
            if self.head.next == self.head:  # Single node case
                self.head = None
            else:
                self.head = self.head.next
                current.next = self.head
        else:
            current = self.head
            while current.next != self.head and current.next.data != data:
                current = current.next

            if current.next.data == data:
                current.next = current.next.next

    def display(self):
        elements = []
        current = self.head
        if current:
            while True:
                elements.append(current.data)
                current = current.next
                if current == self.head:
                    break
        print(" -> ".join(map(str, elements)))

    def search(self, target):
        if self.is_empty():
            return False

        current = self.head
        while True:
            if current.data == target:
                return True
            current = current.next
            if current == self.head:
                break

        return False

# Example usage:
my_circular_linked_list = CircularLinkedList()
my_circular_linked_list.append(1)
my_circular_linked_list.append(2)
my_circular_linked_list.append(3)
my_circular_linked_list.prepend(0)

my_circular_linked_list.display()  # Output: 0 -> 1 -> 2 -> 3

my_circular_linked_list.delete(2)
my_circular_linked_list.display()  # Output: 0 -> 1 -> 3
