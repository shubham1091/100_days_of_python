import art

def add(n1, n2):
    """ adds two numbers together """
    return n1 + n2


def subtract(n1, n2):
    """ subtracts two numbers together """
    return n1 - n2


def divide(n1, n2):
    """ deviate two numbers together """
    if n2 == 0:
        return -1
    return n1/n2


def multiply(n1, n2):
    """ multiply two numbers together """
    return n1*n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculate():
    print(art.logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operation:
        print(symbol,end=",  ")
    print()

    while True:
        operation_symbol = input("Pick a operation: ")
        num2 = float(input("What's the next number?: "))

        fun = operation[operation_symbol]
        answer = fun(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        ck = input(f"Type 'y' to continue calculatin with {answer}, or type 'n' to start a new calculation : ")
        if ck == 'y':
            num1 = answer
        elif ck == 'n':
            calculate()
            break
        else:
            break

calculate()