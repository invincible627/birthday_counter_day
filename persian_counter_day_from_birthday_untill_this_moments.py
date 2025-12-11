print('سلام!')

year = int(input('سال را وارد کنید: '))
month = int(input('ماه را وارد کنید: '))
day = int(input('روز را وارد کنید: '))
year1 = int(input('سال فعلی را وارد کنید: '))
month1 = int(input('ماه فعلی را وارد کنید: '))
day1 = int(input('روز فعلی را وارد کنید: '))
answer_year1 = (year1 - year) * 365
answer_month1 = (month1 - month) * 30
answer_day1 = day1 - day
result = answer_year1 + answer_month1 + answer_day1
if day > day1:
    answer_month1 -= 1
    answer_day1 = (30 - day) + day1
result = answer_year1 + answer_month1 + answer_day1
print(result)