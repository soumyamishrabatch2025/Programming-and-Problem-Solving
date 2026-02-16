class Complex:
	# Write the code......
	def __init__(self):
		self.real = self.img = 0
		
	def initComplex(self):
		self.real, self.img = list(map(int,input().split(" ")))

	def sum(self, a, b):
		self.real = a.real + b.real
		self.img = a.img + b.img

	def display(self):
		if self.img >= 0:
			print(f"{self.real} + {self.img}i")
		else:
			print(f"{self.real} - {-self.img}i")
			


# Create three instances
c1 = Complex()
c2 = Complex()
c3 = Complex()

# Initialize two complex numbers
c1.initComplex()
c2.initComplex()

# Compute and display sum
c3.sum(c1, c2)
c3.display()