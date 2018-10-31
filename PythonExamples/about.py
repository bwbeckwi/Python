
'''
(*args)     arguments
(**kwargs)  key word arguments
'''


def about(name,age,likes):
    sentence = "Meet {}! They are {} years old and they like {}.".format(name,age,likes)
    return sentence


def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))


dictionary = {"name":"Brad", "age":23, "likes":"Python"}
print(about(**dictionary))

foo(Lori = "Female", Brad = "male")
        
