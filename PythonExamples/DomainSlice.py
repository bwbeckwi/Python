# Email Slicer

email = input("What is your email address?:")
user = email[:email.index("@")]
domain = email[email.index("@") + 1:]
output = "Your username is {} and your Email domain is {}".format(user,domain)
print(output)
