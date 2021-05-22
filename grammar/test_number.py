import unittest

class TestFloat(unittest.TestCase):
  def test_round_float_two_digits(self):
    my_number = 1570.539999999996
    formatted_float = round(my_number, 2)
    self.assertEqual(formatted_float, 1570.54)