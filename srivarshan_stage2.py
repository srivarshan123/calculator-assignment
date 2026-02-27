# Stage 2 - Extended Calculator with Result Classification

print("Extended Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = None

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2

else:
    print("Invalid operator.")

if result is not None:
    print("Result:", result)

    if result > 0:
        print("The result is Positive.")
    elif result < 0:
        print("The result is Negative.")
    else:
        print("The result is Zero.")
