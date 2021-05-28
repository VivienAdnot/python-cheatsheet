import unittest
import random

class TestRandom(unittest.TestCase):
  # can return 0 and 10 as well
  def test_generate_integer_between_0_and_10(self):
    magic_number = random.randint(0, 10)
    self.assertLessEqual(magic_number, 10)
    self.assertGreaterEqual(magic_number, 0)

  def test_generate_negative_integer(self):
    magic_number = random.randint(-10, -1)
    self.assertLessEqual(magic_number, -1)
    self.assertGreaterEqual(magic_number, -10)
