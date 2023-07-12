import unittest

class TestListComprehension(unittest.TestCase):
  def test_square(self):
    square = [x**2 for x in range(5)]
    self.assertEqual(square, [0,1,4,9,16])