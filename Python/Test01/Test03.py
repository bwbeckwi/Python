# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep


def main():
    clear()
    # sleep(1)
    open_myfile("C:/tmp/ServerList.txt")
    # print(raise_to_power(3,4))


def open_myfile(file_path):
    if file_path:
        with open(file_path, "r", newline="") as f:
            items = f.read()
            item_list = items.split("\r\n")
            for item in item_list:
                # print(type(item)) # Example of type
                # print(dir(item))  # Example of parameters and functions
                #print("\r\n")
                # item = item.replace('\x0c', '')
                item = item.replace('\00', '')
                item = item.replace('\x0a-\x0c', '')
                item = item.replace('\x5e', '')
                print(item.upper())
    else:
        print("File not found! ")

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return '\r\n' + str(result)


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


if __name__ == "__main__":
    main()

