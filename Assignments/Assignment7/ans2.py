import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z0-9\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Example usage
emails = ["abc@gmail.com", "xyz.k@ibm.com", "abc_get@wipro.com"]
valid_emails = [email for email in emails if validate_email(email)]
print(valid_emails)  # Output: ['abc@gmail.com', 'xyz.k@ibm.com', 'abc_get@wipro.com']
