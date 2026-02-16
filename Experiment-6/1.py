# Type Content here...
import datetime

day = int(input())
month = int(input())
year = int(input())
delta = datetime.timedelta(1)

try:
	next_date = datetime.date(year, month, day) + delta
	print(f"{next_date.day // 10}{next_date.day % 10}-{next_date.month // 10}{next_date.month % 10}-{next_date.year}")
except ValueError:
	print("Invalid Date")

