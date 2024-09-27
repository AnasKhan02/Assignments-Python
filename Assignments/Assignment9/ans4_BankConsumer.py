from ans3_dotted_line_decorator import dotted_line_decorator

class BankConsumer:
    @dotted_line_decorator
    def transaction_details(self, transaction_id, amount):
        print(f"Transaction ID: {transaction_id}, Amount: {amount}")

if __name__ == "__main__":
    bank_consumer = BankConsumer()
    bank_consumer.transaction_details("TX123456", 250.75)
