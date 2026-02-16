# Type Content here...

a = int(input())
b = int(input())
flag = True
no_prime = True

for i in range(a, b+1):
	flag = True
	if i <= 1:
		continue
	for j in range(2, i):
		if i % j == 0:
			flag = False
			break
	if flag == True:
		no_prime = False
		print(i)
		
if no_prime == True:
	print("No primes")
		