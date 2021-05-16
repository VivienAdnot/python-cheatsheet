import unittest

class TestGrammar(unittest.TestCase):
  def func(self, value):
    if (value % 2):
      return True
    raise ValueError('value must be odd')

  def test_try_catch_should_pass(self):
    try:
      self.assertEqual(self.func(123), True)
    except ValueError as err:
      self.assertEqual(err, 1)

  def test_try_catch_should_break(self):
    try:
      result = self.func(120)
      # this line is never ran
      self.assertEqual(result, False)
    except ValueError as err:
      self.assertEqual(err.args[0], 'value must be odd')
