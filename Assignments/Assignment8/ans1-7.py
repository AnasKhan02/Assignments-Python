# 1. Write a Python program to create a singly linked list, append some items and iterate through the list.


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def iterate(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# Example usage
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.iterate()

# 2. Write a Python program to find the size of a singly linked list.

def size_of_list(sll):
    count = 0
    current = sll.head
    while current:
        count += 1
        current = current.next
    return count

# Example usage

print("\n","-"*50)
print(size_of_list(sll))

# 3. Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false.

def search_item(sll, target):
    current = sll.head
    while current:
        if current.data == target:
            return True
        current = current.next
    return False

# Example usage
print(search_item(sll, 2))  # True
print(search_item(sll, 4))  # False

# 4. Write a Python program to access a specific item in a singly linked list using index value.

def search_by_index(sll, target_index):
    current = sll.head
    index = 1
    while current:
        if index == target_index:
            return current.data
        index = index + 1
        current = current.next
    return -1

print(search_by_index(sll, 1))

# 5. Write a Python program to set a new value of an item in a singly linked list using index value.

def set_val_by_index(sll, target_index, value):
    current = sll.head
    index = 1
    while current:
        if index == target_index:
            current.data = value
            return
        index = index + 1
        current = current.next
    return -1

set_val_by_index(sll, 1, 19)
print(search_by_index(sll, 1))

# 6. Write a Python program to delete the first item from a singly linked list.

def delete_first(sll):
    if sll.head:
        sll.head = sll.head.next

# Example usage
delete_first(sll)
sll.iterate()

# 7. Write a Python program to delete the last item from a singly linked list.

def delete_last(sll):
    current = sll.head
    if not current.next:
        sll.head = sll.head.next
    while current.next.next:
        current = current.next
    current.next = None

# Example usage
print("\n","-"*50)
delete_last(sll)
sll.iterate()