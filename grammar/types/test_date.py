from datetime import date
import unittest

def convert_month_index_to_string(month_index):
  return date(1900, month_index, 1).strftime('%B')

class TestDate(unittest.TestCase):
  # def test_get_current_date(self):
  #   today = date.today()
  #   self.assertEqual(today.year, 2021)
  #   self.assertEqual(today.month, 5)
    # self.assertEqual(today.day, 22)

  def test_get_15_years_ago(self):
    today = date.today()
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