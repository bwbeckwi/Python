import numba


@numba.jit("void(f4[:])")
def bubblesort(x):

    for end in range(len(x), 1, -1):

        for i in range(end - 1):

            cur = x[i]

            if cur > x[i + 1]:

                tmp = x[i]
                x[i] = x[i + 1]
                x[i + 1] = tmp


print('LLVM IR'.center(120, '-'))
for v, k in bubblesort.inspect_llvm().items():
    print(v, k)

print('ASM'.center(120, '-'))
for v, k in bubblesort.inspect_asm().items():
    print(v, k)
