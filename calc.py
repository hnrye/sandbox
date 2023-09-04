#ultra-basic_calculator

num1 = float(input())
op = str(input())
num2 = float(input())

if op == "+":
    print(f"result of {num1}{op}{num2} is {num1 + num2}")
elif op == "/":
    print(f"result of {num1}{op}{num2} is {num1 / num2}")
elif op == "-":
    print(f"result of {num1}{op}{num2} is {num1 - num2}")
elif op == "*":
    print(f"result of {num1}{op}{num2} is {num1 * num2}")
elif op == "//":
    print(f"result of {num1}{op}{num2} is {num1//num2}")
elif op == "%":
    print(f"result of {num1}{op}{num2} is {num1%num2}")
else:
    print("error:invalid_input")