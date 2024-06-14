# Create a Node class to create a node
class Node:
    def __init__(self, data):  # Corrected the init method
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):  # Corrected the init method
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
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

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list at given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while current_node is not None and position != index:
                position += 1
                current_node = current_node.next

            if current_node is not None:
                current_node.data = val
            else:
                print("Index not present")

    # Method to remove the first node of linked list
    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    # Method to remove the last node of linked list
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

    # Method to remove a node at given index
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

    # Method to remove a node from linked list by value
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

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    # Print method for the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# Create a new linked list
llist = LinkedList()

# Add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# Print the linked list
print("Node Data")
llist.printLL()

# Remove nodes from the linked list
print("\nRemove First Node")
llist.remove_first_node()
llist.printLL()

print("\nRemove Last Node")
llist.remove_last_node()
llist.printLL()

print("Remove Node at Index 1")
llist.remove_at_index(1)
llist.printLL()

# Update a node in the linked list
print("\nUpdate node Value")
llist.updateNode('z', 0)
llist.printLL()

# Print the size of the linked list
print("\nSize of linked list:", llist.sizeOfLL())
