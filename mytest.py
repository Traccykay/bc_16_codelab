def prime_no(number):
	"""prime number checker"""
	if type(number) != int:
		return False
	if number == 2 or number ==3:
		return True
	elif number < 2 or number % 2 == 0:
		return False
	elif number < 9:
		return True
	elif number % 3 == 0:
		return False
    
