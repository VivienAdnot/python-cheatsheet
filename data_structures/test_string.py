import unittest

class TestString(unittest.TestCase):
  def test_string_with_variable(self):
    var = 123
    str = f'a string containing {var}'
    self.assertEqual(str, 'a string containing 123')