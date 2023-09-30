import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        
        if password_length < 8:
            print("Password length should be at least 8 characters.")
        else:
            password = generate_password(password_length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")
