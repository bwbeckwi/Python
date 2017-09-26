import numpy as np
import timeit


def bubblesort(x):

    for end in range(len(x), 1, -1):

        for i in range(end - 1):

            cur = x[i]

            if cur > x[i + 1]:

                tmp = x[i]
                x[i] = x[i + 1]
                x[i + 1] = tmp


original = np.arange(0.0, 10.0, 0.01, dtype='f4')
shuffled = original.copy()
np.random.shuffle(shuffled)

sorted = shuffled.copy()
bubblesort(sorted)

print(timeit.timeit('bubblesort(sorted)', setup='from __main__ import bubblesort, sorted', number=100))
