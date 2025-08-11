# Simple calculator: two numbers and an operation

# Collect inputs
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("Choose operation (+, -, *, /): ").strip()

# Compute based on the chosen operation
if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    if b == 0:
        print("Error: Division by zero is not allowed.")
        raise SystemExit
    result = a / b
else:
    print("Invalid operation. Please choose one of +, -, *, /.")
    raise SystemExit

# Display the result in the requested format
print(f"{a:g} {op} {b:g} = {result:g}")
# 🎉 Welcome to the Fun Calculator! 🎉