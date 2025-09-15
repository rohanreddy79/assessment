# Package Sorting Assessment

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

To run the unit tests, ensure you have Python 3 installed and
execute:

```bash
python3 -m unittest test_package_sorter.py -v
```

This will execute all test cases in verbose mode.

## Usage

Import the `sort` function from `package_sorter` and call it with
numeric arguments for width, height, length (in centimeters) and mass
(in kilograms). The function returns a string indicating the
appropriate stack.

```python
from package_sorter import sort

category = sort(100, 100, 50, 10)
print(category)  # prints "SPECIAL"
```

Use this repository as a starting point for the assessment. Feel free
to modify or extend the code and tests as needed.