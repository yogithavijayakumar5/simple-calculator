def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    while True:
        num1 = get_number("Enter first number: ")
        op = input("Enter operation (+, -, *, /): ")
        num2 = get_number("Enter second number: ")

        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operation")
            continue

        print(f"Result: {result}")

        again = input("Do another calculation? (y/n): ")
        if again.lower() != "y":
            break

if __name__ == "__main__":
    main()
