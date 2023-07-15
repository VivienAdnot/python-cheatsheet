import unittest

class TestCast(unittest.TestCase):
  def test_cast_string_to_number(self):
    my_str = '1570'
    my_number = int(my_str)
    self.assertEqual(isinstance(my_number, int), True)