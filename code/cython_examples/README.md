# Cython

Detailed documentation on Cython can be found [here](http://cython.org/).

## Running the Example(s)

Compile the ```primes.pyx``` into C source and a shared object.

```bash
python setup.py build_ext --inplace
```

Run the ```call_primes.py``` script to invoke the C-extension version of the primes function.

```bash
python call_primes.py
```
