import unittest

class TestString(unittest.TestCase):
  def test_string_with_variable(self):
    var = 123
    str = f'a string containing {var}'
    self.assertEqual(str, 'a string containing 123')

  def test_format_float_as_currency(self):
    my_number = 1570.539999999996
    formatted_float = "${:,.2f}".format(my_number)
    self.assertEqual(formatted_float, '$1,570.54')