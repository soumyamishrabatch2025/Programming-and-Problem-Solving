
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def get_days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap(year) else 28
    else:
        return 0 # Invalid month

def get_next_day(day, month, year):
    days_in_current_month = get_days_in_month(month, year)
    
    if day < days_in_current_month:
        return day + 1, month, year
    else:
        if month < 12:
            return 1, month + 1, year
        else:
            return 1, 1, year + 1

def validate_and_increment_date(day, month, year):
r
    if year <= 0:
        print("Invalid Date")
        return
    

    days_in_month = get_days_in_month(month, year)
    if days_in_month == 0:
        print("Invalid Date")
        return
    
    if not (1 <= day <= days_in_month):
        print("Invalid Date")
        return
    
    next_day, next_month, next_year = get_next_day(day, month, year)
    
    print(f"{next_day:02d}-{next_month:02d}-{next_year:04d}")


try:
    day_input = int(input())
    month_input = int(input())
    year_input = int(input())
    
    validate_and_increment_date(day_input, month_input, year_input)

except ValueError:
    print("Invalid Date")




