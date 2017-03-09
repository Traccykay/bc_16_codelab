import unittest
from functions import my_functions

class Test_math(unittest.TestCase):
	"""docstring for math_Functions"""
	def test_add(self):
		self.assertTrue(my_functions(10,20,"+"),30)
	def test_sub(self):
		self.assertTrue(my_functions(5,3, "-"),2)
	def test_multiply(self):
		self.assertTrue(my_functions(7,5, "*"),35)
	def test_div(self):
		self.assertTrue(my_functions(56,7, "//"), 8)
	def test_modulus(self):
		self.assertFalse(my_functions(8,4, "%"), 0)

if __name__=="__main__":
	unittest.main()