import unittest
import math

class TestFloor(unittest.TestCase):
  def test_floor(self):
    self.assertEqual(math.floor(5 / 2), 2)