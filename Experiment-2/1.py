# Write your code here...
from math import sqrt

def find_roots(a: int, b: int, c: int):

	D = (b ** 2) - (4 * a * c)

	if (D > 0):
		root1 = (- b + sqrt(D)) / (2 * a) 
		root2 = (- b - sqrt(D)) / (2 * a) 
		print(f"root1 = {root1:.2f}")
		print(f"root2 = {root2:.2f}")
	elif (D == 0):
		root = -b / (2 * a)
		print(f"root1 = root2 = {root:.2f}")
	else:
		real = -b / (2 * a)
		img = sqrt(-((b**2) - (4 * a * c))) / (2 * a)
		print(f"root1 = {real:.2f}+{img:.2f}i\nroot2 = {real:.2f}-{img:.2f}i\n")
		

a, b, c = list(map(int, input().split(" ")))
find_roots(a, b, c)
