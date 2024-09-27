class Parent:
    pass

class Child(Parent):
    pass

# Check if Child is a subclass of Parent
print(issubclass(Child, Parent))  # Output: True
print(issubclass(Parent, Child))  # Output: False
