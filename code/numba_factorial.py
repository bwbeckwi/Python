from numba import int32, jit


@jit(int32(int32), nopython=True)
def factorial(x):

    if x <= 1:

        return 1

    else:

        return x * factorial(x - 1)


@jit
def fact_10():

    return factorial(10)


print(fact_10())
