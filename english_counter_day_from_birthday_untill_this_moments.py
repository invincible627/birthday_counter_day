print('hello')
year = int(input('enter the year'))
month =  int(input('enter the month'))
day = int(input('enter the day'))
year1 = int(input('enter the current year'))
month1 = int(input('enter the current month'))
day1 = int(input('enter the current day'))
answer_year1 = (year1 - year) * 365
answer_month1 = (month1 - month) * 30
answer_day1 = day1 - day
result = answer_year1 + answer_month1 + answer_day1
if day > day1:
    answer_month1 -= 1
    answer_day1 = (30 - day) + day1
result = answer_year1 + answer_month1 + answer_day1
print(result)