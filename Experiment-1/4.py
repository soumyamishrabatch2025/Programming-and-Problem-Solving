# Write your code here...

def calc_area(base: float, height: float) -> float:
	return 0.5 * height *  base

base = float(input())
height = float(input())
area = calc_area(base, height)

print(f"{area:.2f}")