# Write your code here.....

def generate_fibonacci_sequence(n: int):

	series = [0, 1]
	sum = 1

	while sum <= n:
		series.append(sum)
		sum = series[-1] + series[-2]

	return series
		