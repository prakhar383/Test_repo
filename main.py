from add import add
from subtract import subtract

def main():
    print("=== Simple Python Calculator ===")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return

    print("\nSelect Operation:")
    print("1. Add")
    print("2. Subtract")
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == '1':
        result = add(num1, num2)
        print(f"\nResult: {num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"\nResult: {num1} - {num2} = {result}")
    else:
        print("\nInvalid choice. Please select 1 or 2.")


a = 10
b = 7
#test comment

if __name__ == "__main__":
    main()
