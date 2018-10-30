import os


name = input("Enter computer name: ")
print(os.system("ping -t " + name))

