def choose_operation():
    print("Which operation would you like to perform?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice: ")
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    if choice == "1":
        result = add(first_number, second_number)
    elif choice == "2":
        result = subtract(first_number, second_number)
    elif choice == "3":
        result = multiply(first_number, second_number)
    elif choice == "4":
        result = divide(first_number, second_number)
    else:
        result = "Invalid choice."

    print("Result:", result)

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b

def main():
    choose_operation()

main()

