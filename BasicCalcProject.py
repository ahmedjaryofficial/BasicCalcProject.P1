num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
Operation = input("Enter the operation (+, -, *, /): ")
if num2 == 0 and Operation == '/':
    print("Error: Division by zero is not allowed.")
else:
    if Operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif Operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif Operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif Operation == '/':
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Invalid operation. Please enter one of the following: +, -, *, /.")