def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

def calculator():
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    shouldContinue = True

    while shouldContinue:
        operationSymbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculationFunc = operations[operationSymbol]
        answer = calculationFunc(num1, num2)

        print(f"{num1} {operationSymbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit: ") == "y":
            num1 = answer
        else:
            shouldContinue = False

calculator()
    
