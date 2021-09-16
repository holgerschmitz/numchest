import unittest
import math
import numpy as np

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir + '/src')
print(parentdir)
from numchest import roots

class TestFindZeros(unittest.TestCase):

  def test_sin_index(self):
    x = np.arange(start=0, stop=20, step=0.1)
    s = np.sin(x)
    z = roots.findZeros(s)
    expected = np.array([31.41599463, 62.83169825, 94.24793637, 125.66358431, 157.07973547, 188.49556292])
    self.assertEqual(z.size, expected.size)
    self.assertTrue(np.allclose(z, expected))

  def test_sin_axis(self):
    x = np.arange(start=0, stop=20, step=0.1)
    s = np.sin(x)
    z = roots.findZeros(s, axis=x)
    expected = np.array([3.141599463, 6.283169825, 9.424793637, 12.566358431, 15.707973547, 18.849556292])
    self.assertEqual(z.size, expected.size)
    self.assertTrue(np.allclose(z, expected))

  def test_sin_limits(self):
    x = np.arange(start=0, stop=20, step=0.1)
    s = np.sin(x)
    z = roots.findZeros(s, axis=x, start=35, end=-20)
    expected = np.array([6.283169825, 9.424793637, 12.566358431, 15.707973547])
    self.assertEqual(z.size, expected.size)
    self.assertTrue(np.allclose(z, expected))


if __name__ == '__main__':
  unittest.main()