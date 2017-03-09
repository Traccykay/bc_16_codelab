def find_max_min(number):
  minimum = number[0]
  maximum = number[1]
  if type(number) == list:
    for numbers in number:
      if numbers < minimum:
        minimum = numbers
      elif numbers > maximum:
        maximum = numbers
    b = []
    if minimum == maximum:
      b.append(len(number))
      return b
    else:
      b.append(minimum)
      b.append(maximum)
      return b
  else:
    return "The input is not a list"