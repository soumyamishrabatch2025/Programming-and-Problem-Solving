# Type Content here...

import numpy as np

dim = int(input("dimension: "))

array1 = []
array2 = []

print("first matrix:")
for i in range(dim):
	array1.append(list(map(int, input().split(" "))))
	
print("second matrix:")
for j in range(dim):
	array2.append(list(map(int, input().split(" "))))

array1 = np.array(array1)
array2 = np.array(array2)

print("Resultant Matrix:")
prod = np.matmul(array1, array2)

for row in prod:
	for index, value in enumerate(row):
		print(value, end = " " if dim - 1 != index else "\n")







