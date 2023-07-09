import numpy as np
from numpy.testing import assert_array_equal

# takes a list
def get_3_max_values(arr):
  np_array = np.array(arr)
  sorted_index_array = np.argsort(np_array)
  sorted_array = np_array[sorted_index_array]

  indices = sorted_index_array[-3:]
  result = sorted_array[-3:]
  return indices, result

class TestNumpy:
  # should return 3 mac values from array
  def test_get_3_max_values(self):
    values = [-3.89, -59.99, 2.83, 7.53, 13.58, -9.29, 4.6, 10.48, 6.79, -5.8, 9.01]
    largest_indices, largest_values = get_3_max_values(values)
    assert_array_equal(largest_values, [9.01, 10.48, 13.58])
    assert_array_equal(largest_indices, [10, 7, 4])

  # cumsum add the current element of array with previous element
  def test_cumsum(self):
    values = [4, 6, 12]
    expected_result = [4, 4+6, 4+6+12] # [4, 10, 22]
    assert_array_equal(np.cumsum(values), expected_result)