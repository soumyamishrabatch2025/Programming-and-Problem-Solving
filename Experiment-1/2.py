# Type Content here...

def calc_are(length: float, width: float) -> float :
	return length * width

length = float(input())
width = float(input())
area = calc_are(length, width)

print(f"{area:.2f}")
