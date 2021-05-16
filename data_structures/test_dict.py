from typing import List
import unittest

class PortfolioLine:
  # asset: Asset
  ticker: str
  units: int
  book_price: float # euros ?
  market_price: float # euros ?

  def __init__(self, ticker, units, book_price):
    self.ticker = ticker
    self.units = units
    self.book_price = book_price # the price where we bought the asset
    self.market_price = book_price # the current price of the asset

  def latent_gain(self):
    total_book_value = self.units * self.book_price
    total_market_value = self.units * self.market_price
    return total_market_value - total_book_value


class Portfolio:
  lines = {}

  def __init__(self, lines = None):
    self.lines = lines if lines else {}

  def add_line(self, units, ticker, book_price):
    if ticker not in self.lines:
      self.lines[ticker] = { 'values': [] }
    
    self.lines[ticker]['market_price'] = book_price
    self.lines[ticker]['values'].append(PortfolioLine(ticker=ticker, units=units, book_price=book_price))

class TestPorfolio(unittest.TestCase):
  def setUp(self):
    self.portfolio1 = Portfolio()
    self.portfolio1.add_line(units=5, ticker='SPY', book_price=10.00)
    self.portfolio1.add_line(units=2, ticker='SPY', book_price=15.00)
    self.portfolio1.add_line(units=1, ticker='GLD', book_price=70.00)

  def x_test_get_keys(self):
    self.assertEqual(self.portfolio1.lines.keys(), ['SPY', 'GLD'])