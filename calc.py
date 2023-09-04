#ultra-basic_calculator

num1 = input()

if num1 == "help":
    print("commands:\n+\n/\n-\n*\n//\n%")
    num1 = float(input())

num1 = float(num1)
op = str(input())
num2 = float(input())

if op == "+":
    print(f"result of {num1} {op} {num2} is {num1 + num2}")
elif op == "/":
    a = str(input("max.prec? y/n\n"))
    if a == "n":
        print(f"result of {num1} {op} {num2} is {num1 / num2:.3f}")
    elif a == "y":
        print(f"result of {num1} {op} {num2} is {num1 / num2}")
elif op == "-":
    print(f"result of {num1} {op} {num2} is {num1 - num2}")
elif op == "*":
    print(f"result of {num1} {op} {num2} is {num1 * num2}")
elif op == "//":
    print(f"result of {num1} {op} {num2} is {num1 // num2}")
elif op == "%":
    print(f"result of {num1} {op} {num2} is {num1 % num2}")
else:
    print("error:invalid_input")


#if num1%num2 == 1:
#        print("odd num")
#    elif num1%num2 == 0:
#        print("even num")