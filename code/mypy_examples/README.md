# mypy

Detailed documentation on mypy can be found [here](http://mypy-lang.org/index.html).

## Running the Example(s)

See the standard version of the code ```mypy_dynamic_example.py```, this code does not include any type hints. Running ```mypy``` on this code will have no effect.

Now look at version of the code with type hints ```mypy_static_example.py```, which allows for ```mypy``` to perform static analysis on the code. If type-checking passes, ```mypy``` will not print anything. If there is an issue, it will be reported.

```bash
mypy mypy_static_example.py
```

In either case, the static analysis will not affect how the Python interpreter executes the code. It only enforces dynamic typing. You can invoke either of the two versions of the code, they will yield the same result.

```bash
python mypy_dynamic_example.py
python mypy_static_example.py
```
