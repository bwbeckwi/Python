# Author:   Brad Beckwith
# Date:     April 5, 2018
""" Allows the user to run basic calculator operations with two numbers """

def mul(x,y):
    """Returns x * y"""
    return x * y


def div(x,y):
    """Returns x / by y"""
    try:
        return x / y
    except ZeroDivisionError:
        print("Handled div by zero. Returning Zero")
        return 0

def add(x,y):
    """Returns x + y"""
    return x + y


def sub(x,y):
    """Returns x - by y"""
    return x - y


def runOP(op,n1,n2):
    """ Operation argument should be passed in as an INT """
    # Determine required operation
    if (op == 1):
        print("Adding...")
        print(add(n1, n2))
    elif (op == 2):
        print("Subtracting...")
        print(sub(n1, n2))
    elif (op == 3):
        print("Multiplying...")
        print(mul(n1, n2))
    elif (op == 4):
        print("Dividing...")
        print(div(n1, n2))
    else:
        print("I don't understand: ")


def main():
    """Allows User to run basic calculator operations with two numbers."""
    user_continue = True
    while user_continue:
        validinput = False
        while not validinput:
            # Get user input
            try:
                n1 = float(input("Enter number 1: "))
                n2 = float(input("Enter number 2: "))
                op = int(input("What do you want to do: 1:Add, 2:Subtract, 3:Multiply, 4:Divide-Enter number: "))
                validinput = True
            except ValueError:
                print("Invalid input. Try again... ")
            except:
                print("Unknown Error")

        runOP(op,n1,n2)

        # Ask User to continue
        user_yn = input('Would you like to run another calculation? ("y" for yes or any other value to exit. )')
        if (user_yn != 'y'):
            user_continue = False
            break
        else:
            continue


main()