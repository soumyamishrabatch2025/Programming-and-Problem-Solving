# Write your code here...

marks = list(map(int, input().split(" ")))
total = sum(marks)
per = sum(marks) / len(marks)

print(total)
print(f"{per:.2f}")

if per > 75:
	print("Distinction")
elif per >= 60:
	print("First Division")
elif per >= 50:
	print("Second Division")
elif per >= 40:
	print("Third Division")
else:
	print("Fail")