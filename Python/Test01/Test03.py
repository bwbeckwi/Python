import string


# Currently not used...
'''
friends = ["Derek", "Chris", "Joe", "Carlos"]

for index in range(5):
    print(index)


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return '\r\n' + str(result)

'''

# print(raise_to_power(3,4))
'''
try:
    # value = 10 / 0
    number = int(input("Enter a Number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
'''


# Read file
# servers = open("C:/temp/servers.txt", "r")


# for server in servers.readlines():
    # server = server.rstrip("\n").upper()
    # print(server, end="\n")

# servers.close()

"""
wrong
try:
    open(filename, "r")
except FileExistsError as e:
    print(e)
finally:
    f.close
"""

def main():
    file_path = "C:/temp/servers.txt"

    with open(file_path, "r", newline="") as f:
        items = f.read()
        item_list = items.split("\r\n")
        for item in item_list:
            print(type(item))
            print(dir(item))
            print(item)


if __name__ == "__main__":
    main()
