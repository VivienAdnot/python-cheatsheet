from typing import List
import unittest

class Portfolio:
  lines: List[int] = []

  def __init__(self, lines = None):
    self.lines = lines if lines else []

  def add(self, value):
    self.lines.append(value)

class TestPorfolio(unittest.TestCase):
  def test_constructor_empty(self):
    portfolio = Portfolio()
    self.assertEqual(len(portfolio.lines), 0)

  def test_add_line(self):
    portfolio = Portfolio()
    portfolio.add(value=10)
    self.assertEqual(len(portfolio.lines), 1)

  def test_constructor_not_empty(self):
    portfolio3 = Portfolio([3])
    self.assertEqual(len(portfolio3.lines), 1)
    portfolio3.add(value=10)
    self.assertEqual(len(portfolio3.lines), 2)