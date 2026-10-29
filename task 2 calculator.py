def calculator():
    print("=" * 35)
    print("      CODSOFT - CALCULATOR")
    print("=" * 35)

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ").strip()

    if choice == '1':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\nInvalid operation selected!")

if __name__ == "__main__":
    calculator()