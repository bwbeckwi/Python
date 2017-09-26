import pprint
from typing import Dict


def words(string: str) -> Dict[str, int]:

    words_dict = {} # type: Dict[str, int]

    for char in string:

        if char in words_dict:

            words_dict[char] += 1

        else:

            words_dict[char] = 1

    return words_dict


pprint.pprint(words('You just read this sentence. Thanks for reading!'))
