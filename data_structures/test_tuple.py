import unittest

class TestTuple(unittest.TestCase):
  def test_len_tuple(self):
    my_tuple = ((1, 2), (3, 4), (5, 6))
    self.assertEqual(len(my_tuple), 3)