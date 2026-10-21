# Package Sorting Assessment

[![CI](https://github.com/rohanreddy79/assessment/actions/workflows/ci.yml/badge.svg)](https://github.com/rohanreddy79/assessment/actions/workflows/ci.yml)

This repository contains an implementation and test suite for a simple
package‑sorting function as part of an automated warehouse system.

## Overview

The goal is to assign incoming packages to the correct processing stack
based on their dimensions and mass. Packages can be categorized as

- **Bulky**: The product of the package dimensions (volume) is greater
  than or equal to 1,000,000 cm³ **or** any single dimension is at
  least 150 cm.
- **Heavy**: The mass of the package is at least 20 kg.

The `sort()` function places packages into one of three stacks:

| Stack Name | Condition | Action |
|---|---|---|
| `STANDARD` | Package is **neither** bulky **nor** heavy | Can be handled automatically |
| `SPECIAL` | Package is **bulky** *or* **heavy** (but not both) | Requires special handling |
| `REJECTED` | Package is **both** bulky **and** heavy | Rejected by the system |

Invalid inputs (negative numbers, infinities, `NaN` values, or
non‑numeric types) result in a `TypeError` or `ValueError`.

## Files

* **`package_sorter.py`** – Contains the `sort()` function and
  associated helper for input validation. Includes a simple demo when
  run as a script.
* **`test_package_sorter.py`** – A suite of `unittest` cases to
  verify correct behavior under a variety of conditions and boundary
  cases.

## Running the Tests

The code needs only the Python 3 standard library (no `requirements.txt`).
To run the unit tests execute:

```bash
python3 -m unittest test_package_sorter.py -v
```

This will execute all test cases in verbose mode. Verified on this machine
with Python 3.12 (2026-10):

```
$ python3 -m unittest test_package_sorter.py -v
...
Ran 14 tests in 0.000s

OK

$ python3 package_sorter.py
sort(100, 100, 100, 10) -> SPECIAL (expected: SPECIAL)
sort(100, 100, 99, 19.999) -> STANDARD (expected: STANDARD)
sort(150, 10, 10, 5) -> SPECIAL (expected: SPECIAL)
sort(10, 10, 10, 20) -> SPECIAL (expected: SPECIAL)
sort(200, 200, 1, 25) -> REJECTED (expected: REJECTED)
sort(0, 0, 0, 0) -> STANDARD (expected: STANDARD)
```

CI (`.github/workflows/ci.yml`) runs `python -m compileall -q .` and the same
`unittest` command on every push.

## Usage

Import the `sort` function from `package_sorter` and call it with
numeric arguments for width, height, length (in centimeters) and mass
(in kilograms). The function returns a string indicating the
appropriate stack.

```python
from package_sorter import sort

print(sort(100, 100, 50, 10))   # "STANDARD": 500,000 cm³, no side >= 150 cm, 10 kg
print(sort(100, 100, 100, 10))  # "SPECIAL": volume reaches 1,000,000 cm³ (bulky)
print(sort(150, 1, 1, 20))      # "REJECTED": bulky by dimension and heavy
```

Use this repository as a starting point for the assessment. Feel free
to modify or extend the code and tests as needed.

## License

MIT, see [LICENSE](LICENSE).

## Changelog

- 2026-10: corrected the usage example (`sort(100, 100, 50, 10)` is `STANDARD`, not `SPECIAL`); added MIT license, `.gitignore` and CI.
