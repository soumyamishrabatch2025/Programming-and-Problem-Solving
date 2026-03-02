dim = int(input("dimension: "))

array1 = []
array2 = []

print("first matrix:")
for i in range(dim):
	array1.append(list(map(int, input().split(" "))))
	
print("second matrix:")
for j in range(dim):
	array2.append(list(map(int, input().split(" "))))


print("Resultant Matrix:")

prod = []

for i in range(dim):
	prod.append([0 for a in range(dim)])

for i in range(dim):
	for j in range(dim):
		for k in range(dim):
			prod[i][j] += array1[i][k] * array2[k][j]

for row in prod:
	for index, value in enumerate(row):
		print(value, end = " " if dim - 1 != index else "\n")







