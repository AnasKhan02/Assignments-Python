from ans3_dotted_line_decorator import dotted_line_decorator

class DecoratorConsumer:
    @dotted_line_decorator
    def consume_message(self, message):
        print(f"Consuming message: {message}")

if __name__ == "__main__":
    consumer = DecoratorConsumer()
    consumer.consume_message("This is a decorated message.")
