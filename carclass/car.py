class Car:
	"""docstring for Car"""
	def __init__(self, name="General", model="GM", type="saloon"):
		self.type = type
		self.name = name
		self.model = model
		self.num_of_doors = 4
		self.num_of_wheels = 4
		self.speed = 0
		self.moving_speed = 0

		self.car_doors()
		self.car_wheels()



	def car_doors(self):
		if self.name in ["Porshe", "Koenigsegg"]:
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4
		return self.num_of_doors

	def car_wheels(self):
		if self.type == 'trailer':
			self.num_of_wheels = 8
		return self.num_of_wheels

	def is_saloon(self):
		return True if self.type == "saloon" else False
    
	def drive(self, speed):
		if speed == 3:
			self.speed = 1000
		elif speed == 7:
			self.speed = 77
		return self


	





		
      	    




      	   

			
		
      		





      		
  