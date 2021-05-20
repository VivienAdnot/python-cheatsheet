from typing import List
import unittest

class TestDict(unittest.TestCase):
  def setUp(self):
    self.my_dict = { 'foo': 'bar', 'bazob': 'boom' }

  def test_find_key(self):
    self.assertEqual('foo' in self.my_dict, True)
    self.assertEqual(self.my_dict.get('foo'), 'bar')

  def test_get_all_keys(self):
    self.assertEqual(list(self.my_dict.keys()), ['foo', 'bazob'])

  def test_not_found_value_returns_None(self):
    self.assertEqual(self.my_dict.get('fooXXX'), None)
    # other way to write it
    self.assertEqual('fooXXX' in self.my_dict, False)

  def test_append_key_value(self):
    dict2 = {}
    dict2['a'] = 'b'

    print(dict2)
    self.assertEqual(list(dict2.keys()), ['a'])

  def test_append_list(self):
    my_dict = {}
    # init of the list
    my_dict['spy'] = ['hello']
    my_dict['spy'].append('my')
    my_dict['spy'].append('friend')
    self.assertEqual(my_dict['spy'], ['hello', 'my', 'friend'])

  def test_update_list(self):
    my_dict = {}
    # init of the list
    my_dict['spy'] = ['hello']
    my_dict['spy'].append('my')
    my_dict['spy'].append('friend')

    my_dict['spy'][2] = 'dear friend'
    self.assertEqual(my_dict['spy'], ['hello', 'my', 'dear friend'])

  def test_nested_dict(self):
    my_dict = {}
    my_dict['spy'] = {
      'a': 'b',
      'c': []
    }

    my_dict['spy']['c'].append('foo')
    print(my_dict)
    self.assertEqual(my_dict['spy']['c'], ['foo'])