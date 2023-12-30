def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"

        return result

    except ValueError:
        return "Invalid input"

def main():
    print("Simple Calculator")

    num1 = input("Enter first number: ")
    operation = input("Enter operation (+, -, *, /): ")
    num2 = input("Enter second number: ")

    result = calculate(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
