class Node:
    def __init__(self, data):  # Corrected the init method
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):  # Corrected the init method
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while current_node is not None and position + 1 != index:
                position += 1
                current_node = current_node.next

            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return

        if self.head.next is None:  # Special case if there is only one element
            self.head = None
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def remove_at_index(self, index):
        if self.head is None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while current_node is not None and position + 1 != index:
                position += 1
                current_node = current_node.next

            if current_node is not None and current_node.next is not None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    def remove_node(self, data):
        current_node = self.head

        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return

        prev_node = None
        while current_node is not None and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next

        if current_node is not None:
            prev_node.next = current_node.next
        else:
            print("Node with data not found")

    def sizeofLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

llist = LinkedList()

llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex(data='g', index=2)

print("Node Data")
llist.printLL()

print("\nRemove First Node")
llist.remove_first_node()
llist.printLL()

print("\nRemove Last Node")
llist.remove_last_node()
llist.printLL()

#remove a nodes from the linked list
print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print()