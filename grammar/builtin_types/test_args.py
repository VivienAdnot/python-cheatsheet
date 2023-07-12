import unittest

def average(*args):
  return round(sum(args) / len(args), 2)


class TestList(unittest.TestCase):
  def test_average(self):
    self.assertEqual(average(1, 3, 5), 3.0)
    self.assertEqual(average(1, 3, 5, 8), 4.25)
