import pandas as pd
import unittest

data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai', 'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

row_labels = [101, 102, 103, 104, 105, 106, 107]

df = pd.DataFrame(data=data, index=row_labels)

class TestPandas(unittest.TestCase):
  def test_get_city_toronto(self):
    cities = df['city']
    toronto = cities[102]
    self.assertEqual(toronto, 'Toronto')

  def test_get_row_103(self):
    # row is a dict
    row_103 = df.loc[103]
    self.assertEqual(row_103['name'], 'Jana')