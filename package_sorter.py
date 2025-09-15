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
        if not isinstance(v, (int, float)):
            raise TypeError(f"{name} must be int|float; got {type(v).__name__}")
        if v != v or v in (float("inf"), float("-inf")):
            raise ValueError(f"{name} must be finite; got {v!r}")
        if v < 0:
            raise ValueError(f"{name} must be non-negative; got {v}")

def sort(
    width: Number, height: Number, length: Number, mass: Number
) -> Literal["STANDARD", "SPECIAL", "REJECTED"]:
    _validate_non_negative_named(width=width, height=height, length=length, mass=mass)

    volume = width * height * length
    bulky = (volume >= BULKY_VOLUME) or (width >= BULKY_DIM or height >= BULKY_DIM or length >= BULKY_DIM)
    heavy = mass >= HEAVY_MASS

    # keep a ternary to match the original constraint
    result: Stack = Stack.REJECTED if (bulky and heavy) else (Stack.SPECIAL if (bulky or heavy) else Stack.STANDARD)
    return result.value
