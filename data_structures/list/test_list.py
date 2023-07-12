import unittest

class TestList(unittest.TestCase):
  def test_pop(self):
    array = [1, 2, 3, 4]
    test = array.pop(1)
    self.assertEqual(test, 2)
    self.assertEqual(array, [1, 3, 4])

  def test_append(self):
    array = []
    array.append(1)
    self.assertEqual(array, [1])
    self.assertEqual(len(array), 1)

  def test_slice(self):
    array = [2,3,4,5,6]
    self.assertEqual(array[2:4], [4,5])

  def test_get_3_first_elements(self):
    array = [2,3,4,5,6]
    self.assertEqual(array[:3], [2,3,4])

  def test_remove_3_first_elements(self):
    array = [2,3,4,5,6]
    self.assertEqual(array[3:], [5,6])

  def test_sum(self):
    array = [2,3,4,5,6]
    self.assertEqual(sum(array), 20)

  def test_clear(self):
    array = [2,3,4,5,6]
    array.clear()
    self.assertEqual(array, [])