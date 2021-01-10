from django.test import TestCase

from personal.utils import factorial


class FactorialTestCase(TestCase):
    """
    - check negative integer number
    - check zero
    - check 1
    - check positive case (natural number)
    - check float
    - check non-number
    - check large natural number
    """

    # def setUp(self) -> None:
    #     print("SETUP TEST")
    #
    # @classmethod
    # def setUpClass(cls):
    #     print("SETUP CLASS")
    #
    # def tearDown(self) -> None:
    #     print("TEAR TEST")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("TEAR CLASS")
    #
    # def test_001_second(self):
    #     print("NOT SECOND")
    #
    # def test_002_first(self):
    #     print("NOT FIRST")

    def test_positive_case(self):
        """Test positive case for Factorial"""
        init_value: int = 6
        result_to_compare: int = 720

        fact_result = factorial(init_value)

        self.assertEqual(fact_result, result_to_compare)  #  assert fact_result == result_to_compare
        # self.assertFalse(init_value) ## assert not bool(init_value)
        # self.assertIn(100500, [1,2,3])