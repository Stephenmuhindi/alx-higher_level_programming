#!/usr/bin/python3
import argparse
def calculate(a, operator, b):
    operators = {"+": lambda x, y: x + y,
                 "-": lambda x, y: x - y,
                 "*": lambda x, y: x * y,
                 "/": lambda x, y: x / y if y != 0 else "Error: Division by zero"}
    if operator in operators:
        return operators[operator](a, b)
    else:
        return "Unknown operator. Available operators: +, -, * and /"
def main():
    parser = argparse.ArgumentParser(description="Handle basic arithmetic operations.")
    parser.add_argument("a", type=int, help="First operand")
    parser.add_argument("operator", choices=["+", "-", "*", "/"], help="Arithmetic operator")
    parser.add_argument("b", type=int, help="Second operand")
    args = parser.parse_args()
    result = calculate(args.a, args.operator, args.b)
    print(f"{args.a} {args.operator} {args.b} = {result}")
if __name__ == "__main__":
    main()
