#My First Python Calculator

operator = input("Enter ypur operator ( + - * ? ): ")



num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd Number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 4))
elif operator == "-":
    result = num1 - num2
    print(round(result, 4))
elif operator == "*":
    result = num1 * num2
    print(round(result, 4))
elif operator == "/":
    result = num1 / num2
    print(round(result, 4))

else:
    print(f"{operator} is not a valid operator")