import unittest
from unittest.mock import patch     #patch is context manager

from employee import Employee


class TestEmployee(unittest.TestCase):
     #This method executes only once before all test code execution
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    #This method executes only once after all tests are executed
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    #This method executed for every test for intialization
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Sriram', 'Murthy', 50000)
        self.emp_2 = Employee('Kavitha', 'Murthy', 60000)

    def tearDown(self):
        print('tearDown\n')
        #self.emp_1=None

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Sriram.Murthy@email.com')
        self.assertEqual(self.emp_2.email, 'Kavitha.Murthy@email.com')

        self.emp_1.first = 'Kiran'
        self.emp_2.first = 'Raj'

        self.assertEqual(self.emp_1.email, 'Kiran.Murthy@email.com')
        self.assertEqual(self.emp_2.email, 'Raj.Murthy@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Sriram Murthy')
        self.assertEqual(self.emp_2.fullname, 'Kavitha Murthy')

        self.emp_1.first = 'Kiran'
        self.emp_2.first = 'Raj'

        self.assertEqual(self.emp_1.fullname, 'Kiran Murthy')
        self.assertEqual(self.emp_2.fullname, 'Raj Murthy')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Sriram/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Sriram/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()

