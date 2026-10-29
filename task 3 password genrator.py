import random
import string

def generate_password():
    print("=" * 35)
    print("   CODSOFT - PASSWORD GENERATOR")
    print("=" * 35)

    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Length must be greater than zero.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Characters combination: letters, digits, punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    print("\n" + "-" * 35)
    print(f"Generated Password: {password}")
    print("-" * 35)

if __name__ == "__main__":
    generate_password()