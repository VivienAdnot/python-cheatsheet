import datetime
import unittest
import numpy as np

def convert_month_index_to_string(month_index):
  return datetime.date(1900, month_index, 1).strftime('%B')

# base = datetime.datetime(2005, 2, 1)
# dates = np.array(
#   [base + datetime.timedelta(hours=(2 * i)) for i in range(732)]
# )
def create_date_array(start, length):
  # return np.array(
  #   [start + datetime.timedelta(days=i) for i in range(length)]
  # )
  return [start + datetime.timedelta(days=i) for i in range(length)]

class TestDate(unittest.TestCase):
  # def test_get_current_date(self):
  #   today = date.today()
  #   self.assertEqual(today.year, 2021)
  #   self.assertEqual(today.month, 5)
    # self.assertEqual(today.day, 22)

  def test_get_15_years_ago(self):
    today = datetime.date.today()
    year_15_ago = today.year - 15
    self.assertEqual(year_15_ago, 2006)

  def test_get_month_string_from_int(self):
    self.assertEqual(convert_month_index_to_string(1), 'January')
    self.assertEqual(convert_month_index_to_string(2), 'February')
    self.assertEqual(convert_month_index_to_string(3), 'March')
    self.assertEqual(convert_month_index_to_string(4), 'April')
    self.assertEqual(convert_month_index_to_string(5), 'May')
    self.assertEqual(convert_month_index_to_string(6), 'June')
    self.assertEqual(convert_month_index_to_string(7), 'July')
    self.assertEqual(convert_month_index_to_string(8), 'August')
    self.assertEqual(convert_month_index_to_string(9), 'September')
    self.assertEqual(convert_month_index_to_string(10), 'October')
    self.assertEqual(convert_month_index_to_string(11), 'November')
    self.assertEqual(convert_month_index_to_string(12), 'December')

  def test_create_date_array(self):
    start = datetime.date(2006, 7, 1)
    result = create_date_array(start=start, length=5)
    expected_result = [
      datetime.date(2006, 7, 1),
      datetime.date(2006, 7, 2),
      datetime.date(2006, 7, 3),
      datetime.date(2006, 7, 4),
      datetime.date(2006, 7, 5)
    ]
    print(result)
    self.assertEqual(result, expected_result)