import re

def is_strong_password(password):
    # Check minimum length
    if len(password) < 8:
        return False

    # Check for at least one digit
    if not re.search(r"\d", password):
        return False

    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Check for at least one special character
    if not re.search(r"[^A-Za-z0-9]", password):
        return False

    # All conditions met
    return True

# Ask user to input a password
user_password = input("Enter your password: ")

# Check and print result
if is_strong_password(user_password):
    print("Strong")
else:
    print("Weak")
