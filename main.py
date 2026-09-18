class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def pop(self, element):
        new_node = Node(element)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def StackSize(self):
        return self.size