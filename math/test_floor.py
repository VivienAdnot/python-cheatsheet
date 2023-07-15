import unittest
from math import floor

def truncate_two_digits(number):
  return (floor(number * 100)) / 100.0

class TestFloor(unittest.TestCase):
  def test_floor(self):
    self.assertEqual(floor(5 / 2), 2)

  def test_floor_digits(self):
    self.assertEqual(truncate_two_digits(10 / 3), 3.33)