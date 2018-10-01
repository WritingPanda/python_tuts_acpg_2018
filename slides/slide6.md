# Differences between Python 2 and 3

- `__future__` module
- `print` function
- Integer division
- Unicode
- `xrange`
- Raising and handling exceptions
- `next()` and `.next()`
- So much more now (https://docs.python.org/3/whatsnew/3.0.html)

`__future__`

Module to help with backwards compatibility between Python 3 and 2

`print` functions

From keyword to function, Python 3 requires the parenthesis.

## Integer Division

```python
# python 2
3 / 2
# > 1

# python 3
3 / 2
# > 1.5
```

## Unicode

Python 3 treats strings as unicode

Python 2 treats strings as ASCII unless you specify the encoding.

`xrange`

`xrange` was an improvement of the `range` function in Python 2.

Python 3 uses `range`, which is an implementation of `xrange`. Therefore, `xrange` as a function does not exist in Python 3.

## Raising and Handling Exceptions

```python
# Python 2
raise IOError, "file error"
# OR
raise IOError("file error")

# Python 3
raise IOError("File error")
# Only one way to do it
```

```python
# Error Handling

# Python 2
try:
    error_variable
except NameError, e:
    print e, 'the error message'

# Python 3
try:
    error_variable
except NameError as e:
    Print(e, 'the error message')
```

`next()` and `.next()` methods

```python
# Python 2
gen = (letter for letter in 'abcdefg')
next(gen)
gen.next()

# Python 3
gen = (letter for letter in 'abcdefg')
next(gen)
# there is no .next() in python 3
```
