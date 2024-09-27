class Sample:
    class_variable = 10  # Class variable

    def __init__(self):
        self.instance_variable = 20  # Instance variable

# Example usage
sample = Sample()
properties = [attr for attr in dir(Sample) if not attr.startswith('__')]
print(properties)  # Output: ['class_variable', ...]
