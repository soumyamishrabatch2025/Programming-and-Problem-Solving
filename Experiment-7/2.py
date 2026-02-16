# Type Content here...

nums = list(map(int, input().split(" ")))

for index_a, a in enumerate(nums):
	for index_b, b in enumerate(nums):
		if index_a == index_b : continue
		for index_c, c in enumerate(nums):
			if index_c == index_a or index_c == index_b : continue
			print(f"{a}{b}{c}")