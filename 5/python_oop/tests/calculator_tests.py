from unittest import TestCase

from managers.calculator import Calculator


class CalculatorTests(TestCase):
    def testClassInit(self):
        x = Calculator()
        assert x.result is None, \
            "Field result in class should be None after init"

    def test_add_value(self):
        x = Calculator()
        x.add_values(4, 5)
        assert x.result == 9, \
            "Method for adding values returns wrong values"