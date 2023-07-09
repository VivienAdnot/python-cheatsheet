from math import floor
import unittest

class Currency:
  value: float

  def __init__(self, amount = 0.0):
    self.value = self.truncate_two_digits(amount)

  def truncate_two_digits(self, number):
    return (floor(number * 100)) / 100.0

  def __add__(self, other):
    if (type(other) == Currency):
      return Currency(self.truncate_two_digits(self.value + other.value))
    return Currency(self.truncate_two_digits(self.value + other))

  def __sub__(self, other):
    if (type(other) == Currency):
      return Currency(self.truncate_two_digits(self.value - other.value))
    return Currency(self.truncate_two_digits(self.value - other))

  def __mul__(self, other):
    if (type(other) == Currency):
      return Currency(self.truncate_two_digits(self.value * other.value))
    return Currency(self.truncate_two_digits(self.value * other))

  def __truediv__(self, other):
    if (type(other) == Currency):
      return Currency(self.truncate_two_digits(self.value / other.value))
    return Currency(self.truncate_two_digits(self.value / other))

class TestCurrency(unittest.TestCase):
  def test_ctor(self):
    currency1 = Currency(20 / 3)
    self.assertEqual(currency1.value, 6.66)

  def test_add_currency(self):
    currency1 = Currency(20 / 3)
    self.assertEqual(currency1.value, 6.66)
    currency2 = Currency(10 / 3)
    self.assertEqual(currency2.value, 3.33)

    result = currency1 + currency2
    self.assertEqual(result.value, 9.99)

  def test_add_float(self):
    currency1 = Currency(20 / 3)
    result = currency1 + 3
    self.assertEqual(result.value, 9.66)

  def test_substract_currency(self):
    currency1 = Currency(20 / 3)
    self.assertEqual(currency1.value, 6.66)
    currency2 = Currency(10 / 3)
    self.assertEqual(currency2.value, 3.33)

    result = currency1 - currency2
    self.assertEqual(result.value, 3.33)

  def test_substract_float(self):
    currency1 = Currency(20 / 3)
    result = currency1 - 3
    self.assertEqual(result.value, 3.66)

  def test_multiply_currency(self):
    currency1 = Currency(20 / 3)
    self.assertEqual(currency1.value, 6.66)
    currency2 = Currency(10 / 3)
    self.assertEqual(currency2.value, 3.33)

    result = currency1 * currency2
    self.assertEqual(result.value, 22.17)

  def test_multiply_float(self):
    currency1 = Currency(20 / 3)
    result = currency1 * 3
    self.assertEqual(result.value, 19.98)

  def test_divide_currency(self):
    currency1 = Currency(20 / 3)
    self.assertEqual(currency1.value, 6.66)
    currency2 = Currency(10 / 3)
    self.assertEqual(currency2.value, 3.33)

    result = currency1 / currency2
    self.assertEqual(result.value, 2.0)