# Cool features in Python 3

## Advanced unpacking

```python
a, b, *rest = range(10)
```

## Generators

```python
# Only one value is computed at a time
# Low memory impact
# Can break loop in the middle without the need to compute everything

def iterate_bro(n):
    # Turn everything into a generator
    for i in range(n):
        yield from i
```

## Standard Library Additions and Improvements

- faulthandler
    - Display tracebacks when there's a failure
- ipaddress
    - Factory that creates IPs, networks, and interfaces
- functools.lru_cache
    - LRU cache decorator for your functions
    - Can save repeated queries to an external resource whenever the results are expected to be the same
- enum
    - An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.
- Pathlib
```python
# Python 2
import os

directory = "/etc"
filepath = os.path.join(directory, "test_file.txt")

if os.path.exists(filepath):
    print("It's alive!")

# Python 3
from pathlib import Path

directory = Path("/tmp")
filepath = directory / "tmp_file.txt"

if filepath.exists():
    print("It's alive!")
```

For more information, check out https://powerfulpython.com/blog/whats-really-new-in-python-3/. 