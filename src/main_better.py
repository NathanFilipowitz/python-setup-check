from unittest import removeResult

def num_input():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2


def op_input(num1, num2):
    operator = input("Enter an operator (+, -, *, /): ")
    if operator == '+':
        result = add(num1,num2)
        finished = True
        return result, finished
    elif operator == '-':
        result = sub(num1,num2)
        finished = True
        return result, finished
    elif operator == '*':
        result = mul(num1,num2)
        finished = True
        return result, finished
    elif operator == '/':
        if num2 == 0:
            finished = False
            print("Error: Division by zero is undefined.")
        else:
            result = div(num1,num2)
            finished = True
        return result, finished
    else:
        print("Invalid operator.")

def output(result):
    print(f"{result}")

numbers = num_input()
num1 = numbers[0]
num2 = numbers[1]

finished = False

while not finished:
    state = op_input(num1,num2)
    result = state[0]
    finished = state[1]

output(result)