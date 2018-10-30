'''

Written by:     Brad Beckwith
Date:           October 20, 2018
Purpose:        Learn more about Python

'''


from os import system


def ping_host():
    comp_name = input("Enter computer name: ")
    num_tries = input("Enter number of retries: ")
    print(system("ping -n " + num_tries + " " + comp_name))


def main():
    ping_host()


if __name__ == '__main__':
    main()

