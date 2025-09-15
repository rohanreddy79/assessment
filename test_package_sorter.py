"""
Unit tests for the ``sort`` function defined in ``package_sorter``.

These tests verify that packages are classified correctly based on
volume, dimensions, and mass, and that invalid inputs raise
appropriate exceptions.
"""

import unittest

from package_sorter import sort


class TestPackageSorter(unittest.TestCase):
    """Test suite for the package sorting logic."""

    def test_standard(self) -> None:
        """Packages that are neither bulky nor heavy should be STANDARD."""
        self.assertEqual(sort(10, 10, 10, 10), "STANDARD")
        # Volume just under one million (100 × 100 × 99 = 990 000) and mass < 20
        self.assertEqual(sort(100, 100, 99, 19.999), "STANDARD")

    def test_bulky_by_volume_boundary(self) -> None:
        """Exactly one million cubic centimeters should be classified as bulky."""
        self.assertEqual(sort(100, 100, 100, 0), "SPECIAL")

    def test_bulky_by_dimension_boundary(self) -> None:
        """Any dimension equal to 150 cm makes the package bulky."""
        self.assertEqual(sort(150, 1, 1, 0), "SPECIAL")

    def test_heavy_boundary(self) -> None:
        """Mass equal to 20 kg marks a package as heavy."""
        self.assertEqual(sort(1, 1, 1, 20), "SPECIAL")

    def test_rejected_when_both(self) -> None:
        """Packages that are both bulky and heavy are REJECTED."""
        self.assertEqual(sort(200, 200, 1, 25), "REJECTED")

    def test_zero_values(self) -> None:
        """Zero dimensions and mass should not trip special logic."""
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")

    def test_float_inputs(self) -> None:
        """Float values should be handled correctly."""
        self.assertEqual(sort(100.0, 100.0, 100.0, 19.0), "SPECIAL")

    def test_type_and_value_validation(self) -> None:
        """Non‑numeric or negative inputs should raise exceptions."""
        with self.assertRaises(TypeError):
            sort("10", 10, 10, 10)  # Non‑numeric width
        with self.assertRaises(ValueError):
            sort(10, -1, 10, 10)   # Negative height
        with self.assertRaises(ValueError):
            sort(float("inf"), 1, 1, 1)  # Non‑finite width


if __name__ == "__main__":  # pragma: no cover
    unittest.main(verbosity=2)