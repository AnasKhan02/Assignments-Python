class Box:
    def __init__(self, width):
        self.width = width

    def __add__(self, other):
        return Box(self.width + other.width)

    def __gt__(self, other):
        return self.width > other.width

# Example usage
box1 = Box(5)
box2 = Box(10)

box3 = box1 + box2
print(box3.width)  # Output: 15

print(box1 > box2)  # Output: False
