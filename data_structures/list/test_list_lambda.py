import unittest


class TestListLambda(unittest.TestCase):
  # find all numbers divisible by 13
  def test_filter_array(self):
    array = [12, 65, 54, 39, 102, 339, 221, 50, 70]

    result = list(filter(lambda x: x % 13 == 0, array))
    self.assertEqual(result, [65, 39, 221])

  def test_filter_array_of_tuples(self):
    array = [
      # units, ticker, book_price, market_price
      [10, 'SPY', 50.00, 60.00],
      [5, 'SPY', 45.00, 60.00],
      [1, 'GLD', 15.00, 20.00],
    ]

    result = list(filter(lambda columns: columns[1] == 'SPY', array))
    self.assertEqual(len(result), 2)

  def test_filter_array_of_objects(self):
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

    array=[
      LineItem(units=10,ticker='SPY',book_price=50.00,market_price=60.00),
      LineItem(units=5,ticker='SPY',book_price=45.00,market_price=60.00),
      LineItem(units=1,ticker='GLD',book_price=15.00,market_price=20.00),
    ]

    result = list(filter(lambda line: line.ticker == 'SPY', array))
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0].book_price, 50.00)
    self.assertEqual(result[1].book_price, 45.00)

  def test_sort_tuple_asc(self):
    data = [(4,5,6), (1,2,3), (7,8,9)]
    sorted_by_second = sorted(data, key=lambda tup: tup[2])
    self.assertEqual(sorted_by_second, [(1,2,3), (4,5,6), (7,8,9)])

  def test_sort_tuple_desc(self):
    data = [(4,5,6), (1,2,3), (7,8,9)]
    sorted_by_second = sorted(data, key=lambda tup: tup[2], reverse=True)
    self.assertEqual(sorted_by_second, [(7,8,9), (4,5,6), (1,2,3)])