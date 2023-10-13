def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("Python Calculator\n")
    while True:
        print("Menu:\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit\n")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = addition(num1, num2)
            print(f"Result: {num1} + {num2} = {result}\n")

        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtraction(num1, num2)
            print(f"Result: {num1} - {num2} = {result}\n")

        elif choice == "3":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = multiplication(num1, num2)
            print(f"Result: {num1} * {num2} = {result}\n")

        elif choice == "4":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = division(num1, num2)
            print(f"Result: {num1} / {num2} = {result}\n")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
