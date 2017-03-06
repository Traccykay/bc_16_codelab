import math

def primeno(number):
	"""if number < 2: 
		return False"""
	for n in range(0, int(math.srqt(number))+1):
        if number % n == 0:
            return False
        else:
    return True