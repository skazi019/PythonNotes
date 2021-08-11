"""
Practising classes and OOPs
"""

class Robot:

	def __init__(self, name=None, build_year=None) -> None:
		self.name = name
		self.build_year = build_year

	def say_hi(self):
		if self.name:
			print(f"Hi i am {self.name}")
		else:
			print("Robot without name")
	
		if self.build_year:
			print(f"I was built in {self.build_year}")
		else:
			print("year unknown")

	def set_name(self, name):
		self.name = name
	
	def get_name(self):
		return self.name

	def set_build_year(self, build_year):
		self.build_year = build_year
	
	def get_build_year(self):
		return self.build_year
	
	# example of duck typing
	def __len__(self):
		return 90101

x = Robot("Henry", 2020)
y = Robot()

print(x.get_name(), x.get_build_year())
print(y.get_name(), y.get_build_year())

y.set_name('Marvin')

x.say_hi()
y.say_hi()

print(len(x))