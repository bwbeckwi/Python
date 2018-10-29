# Author:   Brad Beckwith
# Date:     April 5, 2018
""" Allows the user to run basic calculator operations with two numbers """

def mul(x,y):
    """Returns x * y"""
    return x * y


def div(x,y):
    """Returns x / by y"""
    return x / y


def add(x,y):
    """Returns x + y"""
    return x + y


def sub(x,y):
    """Returns x - by y"""
    return x - y


def main():
    user_continue = True
    while user_continue:
        while not validinput:
            # Get user input
            try:
                n1 = float(input("Enter number 1: "))
                n2 = float(input("Enter number 2: "))
                op = int(input("What do you want to do: 1:Add, 2:Subtract, 3:Multiply, 4:Divide-Enter number: "))
                validinput = True
            except:
                print("Invalid input. Try again... ")
        # Determine required operation
        if (op == 1):
            print(add(n1, n2))
        elif (op == 2):
            print(sub(n1, n2))
        elif (op == 3):
            print(mul(n1, n2))
        elif (op == 4):
            print(div(n1, n2))
        else:
            print("I don't understand: ")

        # Ask User to continue
        user_yn = input('Would you like to run another calculation? ("y" for yes or any other value to exit.)')
        if (user_yn != 'y'):
            user_continue = False
            break
        else:
            continue

main()