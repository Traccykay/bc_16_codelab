import unittest
from mytest import prime_no

class prime(unittest.TestCase):
	"""docstring for TestCase"""
	
	def test_is_one_prime(self):
		self.assertFalse(prime_no(1))
	def test_is_two_prime(self):
		self.assertTrue(prime_no(2))
	def test_is_a_prime(self):
		self.assertFalse(prime_no('v'))
	def test_is_a_negative_prime(self):
		self.assertFalse(prime_no(-5))
	def test_is_a_float_prime(self):
		self.assertFalse(prime_no(8.5))

if __name__=="__main__":
	unittest.main()
