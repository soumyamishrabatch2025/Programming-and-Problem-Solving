#Write your code here...

def calc_area(r: float) -> float :
	return 3.14 * r * r
radius = float(input())
area = calc_area(radius)

print(f"{area:.4f}")