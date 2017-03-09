
def data_type(a):
  if type(a) == str:
    return len(a)
    
  elif a == None:
    return ("no value")
    
  elif type(a) == bool:
    return bool(a)
    
  elif type(a) == int:
    if a > 100:
      return ("more than 100")
    elif a<100:
      return("less than 100")
    elif a==100:
      return("equal to 100")
      
  elif type(a) == type([]):
    if len(a)==3:
      return a[2]
    else:
      return None 