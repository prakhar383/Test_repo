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
        
    
    
    Test_repo/main.py
    
   
    

    
    choice = input("Enter choice (1, 2, 3, or 4): ").strip()

    if choice == '1':
        result = add(num1, num2)
        print(f"\nResult: {num1} + {num2} = {result}")
    elif choice == '2':
        r
