from ans3_dotted_line_decorator import dotted_line_decorator

@dotted_line_decorator
def display_message(message):
    print(message)

if __name__ == "__main__":
    display_message("Hello, this is a message!")
