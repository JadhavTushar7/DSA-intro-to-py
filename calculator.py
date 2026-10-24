a = float(input("First number: "))
op = input("operator (+,-,*, /): ")
b = float(input("Second number: "))

if op == "+":
   result = a + b

elif op == "-":
    result = a - b

if op == "*":
   result = a * b

if op == "/":
   result = a / b

print(f"{a} {op} {b} = {result}")
