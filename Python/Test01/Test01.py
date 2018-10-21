import os


a = "hello"
b = 123
print(type(a))
print(type(b))

# help(os.path)

print(os.path.isdir("C:\Temp"))
print(os.path.isdir("C:\Tmp"))
print(os.path.isdir("C:\lips"))
print(os.path.isfile("C:\Lips.txt"))
print('Path C:\\tmp exists: ' + str(os.path.exists("C:\tmp")))

# print(os.environ)
print(os.getcwd())
