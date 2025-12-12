class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


def main():
    a, b = map(float, input().split())
    operation = input().strip()

    calc = Calculator()

    if operation == "+":
        ans = calc.add(a, b)
    elif operation == "-":
        ans = calc.sub(a, b)
    elif operation == "*":
        ans = calc.mul(a, b)
    elif operation == "/":
        ans = calc.div(a, b)
    else:
        print("Invalid operation!")
        return

    print(f"{a}{operation}{b} = {ans}")