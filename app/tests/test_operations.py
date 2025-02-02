import unittest

from config import Config
from app import create_app
from app.operations.services import create_list, fibonacci_sum, fibonacci_list

class OperationTestConfig(Config):
  pass

class OperationsTest(unittest.TestCase):

  def setUp(self):
    self.app = create_app(OperationTestConfig)
    self.app_context = self.app.app_context()
    self.app_context.push()

  def tearDown(self):
    self.app_context.pop()

  def test_should_create_a_list_of_elements(self):
    my_list = create_list(1000)
    self.assertEqual(1000, len(my_list))
    # First item
    self.assertEqual(1, my_list[0]["id"])
    self.assertEqual("This is the message number 1", my_list[0]["message"])
    # 100th item
    self.assertEqual(100, my_list[99]["id"])
    self.assertEqual("This is the message number 100", my_list[99]["message"])
    # 1000th item
    self.assertEqual(1000, my_list[999]["id"])
    self.assertEqual("This is the message number 1000", my_list[999]["message"])

  def test_should_aggregate_items_from_a_fibonacci_sequence(self):
    self.assertEqual(0, fibonacci_sum(-1))
    self.assertEqual(0, fibonacci_sum(0))
    self.assertEqual(1, fibonacci_sum(1))
    self.assertEqual(2, fibonacci_sum(2))
    self.assertEqual(4, fibonacci_sum(3))
    self.assertEqual(7, fibonacci_sum(4))
    self.assertEqual(12, fibonacci_sum(5))
    self.assertEqual(143, fibonacci_sum(10))
    self.assertEqual(32951280098, fibonacci_sum(50))
    self.assertEqual(927372692193078999175, fibonacci_sum(100))

  def test_should_get_a_list_of_fibonacci_sequence(self):
    self.assertEqual(0, len(fibonacci_list(-1)))
    list0 = fibonacci_list(0)
    self.assertEqual(1, len(list0))
    self.assertEqual(0, list0[0])
    list1 = fibonacci_list(1)
    self.assertEqual(2, len(list1))
    self.assertEqual(1, list1[1])
    list2 = fibonacci_list(2)
    self.assertEqual(3, len(list2))
    self.assertEqual(1, list2[2])
    list3 = fibonacci_list(3)
    self.assertEqual(4, len(list3))
    self.assertEqual(2, list3[3])
    list4 = fibonacci_list(4)
    self.assertEqual(5, len(list4))
    self.assertEqual(3, list4[4])
    list5 = fibonacci_list(5)
    self.assertEqual(6, len(list5))
    self.assertEqual(5, list5[5])
    list6 = fibonacci_list(6)
    self.assertEqual(7, len(list6))
    self.assertEqual(8, list6[6])
    list7 = fibonacci_list(10)
    self.assertEqual(11, len(list7))
    self.assertEqual(55, list7[10])
    list8 = fibonacci_list(50)
    self.assertEqual(51, len(list8))
    self.assertEqual(12586269025, list8[50])
    list9 = fibonacci_list(78)
    self.assertEqual(79, len(list9))
    self.assertEqual(8944394323791464, list9[78])
    list10 = fibonacci_list(100)
    self.assertEqual(101, len(list10))
    self.assertEqual(354224848179261915075, list10[100])
    list11 = fibonacci_list(300)
    self.assertEqual(301, len(list11))
    self.assertEqual(222232244629420445529739893461909967206666939096499764990979600, list11[300])
