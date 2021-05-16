import unittest

def average(*args):
  return round(sum(args) / len(args), 2)

class TestList(unittest.TestCase):

  def test_average(self):
    self.assertEqual(average(1, 3, 5), 3.0)
    self.assertEqual(average(1, 3, 5, 8), 4.25)

  def test_pop(self):
    arr = [1, 2, 3, 4]
    arr.pop(1)
    self.assertEqual(arr, [1, 3, 4])

  def test_append(self):
    arr = []
    arr.append(1)
    self.assertEqual(arr, [1])
    self.assertEqual(len(arr), 1)