from art import logo


# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    for key in operations:
        print(key)

    again = True

    while again:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        function = operations[operation]
        answer = function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        should_continue = input(
            f"Type 'c' to continue calculating with {answer}\nType 'n' to start a new calculation\nType 'e' to exit.: ")
        if should_continue == "y":
            num1 = answer
        elif should_continue == "n":
            again = False
            calculator()
        else:
            again = False


calculator()
