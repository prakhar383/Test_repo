from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def main():
    print("=== Simple Python Calculator ===")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return

    print("\nSelect Operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    choice = input("Enter choice (1, 2, 3, or 4): ").strip()

    if choice == '1':
        result = add(num1, num2)
        print(f"\nResult: {num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"\nResult: {num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"\nResult: {num1} * {num2} = {result}")
    elif choice == '4':
        try:
            result = divide(num1, num2)
            print(f"\nResult: {num1} / {num2} = {result}")
        except ValueError as e:
            print(f"\nError: {e}")
    else:
        print("\nInvalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()
