import unittest   #Built-in module
import calc


class TestCalc(unittest.TestCase):
    ''' All test code should start with test_xyz(self)'''
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        #Context manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

'''
  We can run without main() using
  >python -m unittest test_calc.py
'''

#if our current application is main()  execution program then run main()
# > python test_calc.py
if __name__ == '__main__':
    unittest.main()

