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

  # find all numbers divisible by 13
  def test_filter(self):
    arr = [12, 65, 54, 39, 102, 339, 221, 50, 70]

    result = list(filter(lambda x: x % 13 == 0, arr))
    self.assertEqual(result, [65, 39, 221])

  def test_filter_arr_tuple(self):
    arr = [
      # units, ticker, book_price, market_price
      [10, 'SPY', 50.00, 60.00],
      [5, 'SPY', 45.00, 60.00],
      [1, 'GLD', 15.00, 20.00],
    ]

    result = list(filter(lambda line: line[1] == 'SPY', arr))
    self.assertEqual(len(result), 2)

  def test_filter_arr_object(self):
    class LineItem:
      units: int
      ticker: str
      book_price: float
      market_price: float

      def __init__(self, units, ticker, book_price, market_price):
        self.units=units
        self.ticker=ticker
        self.book_price=book_price
        self.market_price=market_price

    arr=[
      LineItem(units=10,ticker='SPY',book_price=50.00,market_price=60.00),
      LineItem(units=5,ticker='SPY',book_price=45.00,market_price=60.00),
      LineItem(units=1,ticker='GLD',book_price=15.00,market_price=20.00),
    ]

    result = list(filter(lambda line: line.ticker == 'SPY', arr))
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0].book_price, 50.00)
    self.assertEqual(result[1].book_price, 45.00)

  def test_slice(self):
    arr = [2,3,4,5,6]
    self.assertEqual(arr[2:4], [4,5])