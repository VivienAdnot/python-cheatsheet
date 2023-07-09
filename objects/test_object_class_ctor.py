from typing import List
import unittest

class Portfolio:
  lines: List[int] = []

  def __init__(self, lines = None):
    self.lines = lines if lines else []

  def add(self, value):
    self.lines.append(value)

class TestPorfolio(unittest.TestCase):
  def test_one(self):
    portfolio1 = Portfolio()
    self.assertEqual(len(portfolio1.lines), 0)
    portfolio1.add(value=10)
    self.assertEqual(len(portfolio1.lines), 1)

  def test_two(self):
    portfolio2 = Portfolio()
    self.assertEqual(len(portfolio2.lines), 0)

  def test_three(self):
    portfolio3 = Portfolio([3])
    self.assertEqual(len(portfolio3.lines), 1)
    portfolio3.add(value=10)
    self.assertEqual(len(portfolio3.lines), 2)