from logging import NullHandler

operand1 = None
operator = None
operand2 = None

def main():

    ask_user_input()
    result = calculate(operand1, operator, operand2)
    display_result(result)

def ask_user_input():
    # Get first operand from the user
    global operand1
    operand1 = float(input("Enter the first operand: "))

    # Get the operator from the user
    global operator
    operator = input("Enter an operator (+, -, *, /): ")

    # Get second operand from the user
    global operand2
    operand2 = float(input("Enter the second operand: "))

def calculate(num1, op, num2):
    # Perform the operation based on the operator
    match op:
        case "+":
            res = num1 + num2
            return res
        case "-":
            res = num1 - num2
            return res
        case "*":
            res = num1 * num2
            return res
        case "/":
            if num2 == 0:
                print("Cannot divide by zero")
            res = num1 / num2
            return res
        case "_":
            print("invalid operator")
    return res

def display_result(result):
    # Print the result
    print("Result:", result)


# Call the main function to run the program
main()