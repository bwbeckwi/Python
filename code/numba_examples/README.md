# Numba

Detailed documentation on Numba can be found [here](numba.pydata.org).

## Running the Example(s)

There are two simple examples.

### Bubble Sort

Let's take a bad algorithm and make it faster with brute force. Numba is a frontend compiler that takes decorated Python functions and emits LLVM IR. The LLVM infrastructure takes over and produces highly optimized native code.

First take a look at the standard version of the code ```numba_bubblesort_no_opt.py```. This code makes a large array of floating point numbers, randomizes the array, then sorts it. Average execution time is tracked over a hundred runs.

```bash
python numba_bubblesort_no_opt.py
```

Next take a look at the version of the code with Numba decorators added. This code uses Numba to JIT compile the function bubblesort into LLVM IR, which is then converted into machine code with LLVM. The resulting, highly optimized code is roughly 415x faster.

```bash
python numba_bubblesort_opt.py
```

The LLVM IR and ASM code produced by both Numba and LLVM respectively can be viewed.

```bash
python numba_bubblesort_dis.py
```

### Factorial

This example is structured to the same above, but only Numba code is provided. Some compilers would be able to optimize away everything and compute the factorial of 10 at compile time, this is not the case with Numba. There is still work to be done in this realm.
