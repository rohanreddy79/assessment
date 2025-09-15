from typing import Literal, Union
from enum import Enum

Number = Union[int, float]

BULKY_VOLUME = 1_000_000
BULKY_DIM = 150
HEAVY_MASS = 20


class Stack(str, Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"


def _validate_non_negative_named(**vals: Number) -> None:
    for name, v in vals.items():
        # Explicitly reject bool (since bool is a subclass of int)
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise TypeError(f"{name} must be int|float (not bool); got {type(v).__name__}")
        # Non-finite: NaN or ±inf
        if v != v or v in (float("inf"), float("-inf")):
            raise ValueError(f"{name} must be finite; got {v!r}")
        if v < 0:
            raise ValueError(f"{name} must be non-negative; got {v}")


def sort(
    width: Number, height: Number, length: Number, mass: Number
) -> Literal["STANDARD", "SPECIAL", "REJECTED"]:
    _validate_non_negative_named(width=width, height=height, length=length, mass=mass)

    volume = width * height * length
    bulky_by_volume = volume >= BULKY_VOLUME
    bulky_by_dim = any(d >= BULKY_DIM for d in (width, height, length))
    bulky = bulky_by_volume or bulky_by_dim
    heavy = mass >= HEAVY_MASS

    # Keep a ternary to match the original constraint
    result: Stack = Stack.REJECTED if (bulky and heavy) else (Stack.SPECIAL if (bulky or heavy) else Stack.STANDARD)
    return result.value


if __name__ == "__main__":
    # quick demo
    samples = [
        (100, 100, 100, 10, "SPECIAL"),
        (100, 100, 99, 19.999, "STANDARD"),
        (150, 10, 10, 5, "SPECIAL"),
        (10, 10, 10, 20, "SPECIAL"),
        (200, 200, 1, 25, "REJECTED"),
        (0, 0, 0, 0, "STANDARD"),
    ]
    for w, h, l, m, expected in samples:
        res = sort(w, h, l, m)
        print(f"sort({w}, {h}, {l}, {m}) -> {res} (expected: {expected})")
