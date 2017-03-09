def find_max_min(a):
	if type (a) == list:
		minimum = min(a)
		maximum = max(a)

	if min==max:
		b = len(a)
		return[b]
	else:
		return (maximum, minimum)


	