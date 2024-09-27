# 8. Write a Python program to create a doubly linked list, append some items and iterate through the list (print forward).


class DoubleListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoubleListNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def iterate(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
    def print_reverse_from_node(self, node):
        current = node
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

# Example usage
print("Question 8 Output...")
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.iterate()
print("\n","-"*50,"\n")

# 9. Write a Python program to create a doubly linked list and print nodes from current position to first node.

current_node = dll.head.next  # This is the node with data 2

print("Question 9 Output...")
dll.print_reverse_from_node(current_node)  # Output: 2 1
print("-" * 50)

# 10. Write a Python program to count the number of items of a given doubly linked list.
def count_len(dll):
    count = 0
    current = dll.head
    while current:
        count += 1
        current = current.next
    return count

# Example usage
print("Question 10 Output...")
print(count_len(dll), end=" ")
print("\n","-"*50,"\n")

# 11. Write a Python program to print a given doubly linked list in reverse order.

def print_list_reverse(dll):
    current = dll.head
    while current and current.next:
        current = current.next
    while current:
        print(current.data, end=" ")
        current = current.prev

# Example usage
print("Question 11 Output...")
print_list_reverse(dll)
print("\n","-"*50,"\n")

# 12. Write a Python program to insert an item in front of a given doubly linked list.

def insert_item_front(dll, data):
    new_node = DoubleListNode(data)
    new_node.next = dll.head
    if dll.head:
        dll.head.prev = new_node
    dll.head = new_node

# Example usage
print("Question 12 Output...")
insert_item_front(dll, 0)
dll.iterate()  # 0, 1, 2, 3
print("\n","-"*50,"\n")

# 13. Write a Python program to search a specific item in a given doubly linked list and return true if the item is found otherwise return false.

def search_item(dll, target):
    current = dll.head
    while current:
        if current.data == target:
            return True
        current = current.next
    return False

# Example usage
print("Question 13 Output...")
print(search_item(dll, 2))  # True
print(search_item(dll, 4))  # False
print("-"*50,"\n")

# 14. Write a Python program to delete a specific item from a given doubly linked list.

def delete_item_dll(dll, target):
    current = dll.head
    while current:
        if current.data == target:
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            if current == dll.head:  # Moving head if needed
                dll.head = current.next
            return True
        current = current.next
    return False

# Example usage
print("Question 14 Output...")
delete_item_dll(dll, 2)
dll.iterate()  # 0, 1, 3
print("\n","-"*50,"\n")