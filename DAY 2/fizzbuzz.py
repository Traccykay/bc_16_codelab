def fizz_buzz(number):
  fizz_1="Fizz"
  fizz_2="Buzz"
  fizz_3="FizzBuzz"
    
  if number % 5==0 and number % 3==0:
      return fizz_3

  elif number % 3==0:
      return fizz_1
      
  elif number % 5==0:
      return fizz_2
  else:
      return number
