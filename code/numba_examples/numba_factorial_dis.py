from numba import int32, jit


@jit(int32(int32), nopython=True)
def factorial(x):

    if x <= 1:

        return 1

    else:

        return x * factorial(x - 1)


print('LLVM IR'.center(120, '-'))
for v, k in factorial.inspect_llvm().items():
    print(v, k)

print('ASM'.center(120, '-'))
for v, k in factorial.inspect_asm().items():
    print(v, k)
