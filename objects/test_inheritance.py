from typing import List
import unittest

class Portfolio:
  lines: List[int] = []

  def __init__(self, lines = None):
    self.lines = lines if lines else []

  def add(self, value):
    self.lines.append(value)

class PapaBearPortfolio(Portfolio):
  def remove_by_index(self, index):
    self.lines.pop(index)

class TestPapaBearPortfolio(unittest.TestCase):
  def test_remove_by_index(self):
    papaBearPortfolio = PapaBearPortfolio()
    papaBearPortfolio.add(value=10)
    papaBearPortfolio.add(value=15)
    papaBearPortfolio.add(value=20)
    papaBearPortfolio.remove_by_index(index=1)
    self.assertEqual(papaBearPortfolio.lines, [10, 20])


