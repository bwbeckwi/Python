import pprint


def words(string):

    words_dict = {}

    for char in string:

        if char in words_dict:

            words_dict[char] += 1

        else:

            words_dict[char] = 1

    return words_dict


pprint.pprint(words('You just read this sentence. Thanks for reading!'))
