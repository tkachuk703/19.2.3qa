import pytest
from app.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.сalc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.сalc.multiply(self, 3, 3) == 9