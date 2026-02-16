def sum_of_digits_recursive(n):
	
	# Write your code here
	if n < 10:
		return n
	
	return  int(str(n)[0]) + sum_of_digits_recursive(int(str(n)[1:]))



# Write your code here

number = int(input())
result = sum_of_digits_recursive(number)	
print(result)