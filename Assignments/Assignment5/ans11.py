class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

# Example usage
square = Square(5)
print(square.area())      # Output: 25
print(square.perimeter()) # Output: 20
