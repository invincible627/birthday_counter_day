language = input("Select language. Type pe or persian for Persian, and en or english for English\n")
if language.lower() == "en" or language.lower() == "english":
    print("hello")
    year = int(input("enter the year"))
    month =  int(input("enter the month"))
    day = int(input("enter the day"))
    year1 = int(input("enter the current year"))
    month1 = int(input("enter the current month"))
    day1 = int(input("enter the current day"))
    answer_year1 = (year1 - year) * 365
    answer_month1 = (month1 - month) * 30
    answer_day1 = day1 - day
    result = answer_year1 + answer_month1 + answer_day1
    if day > day1:
        answer_month1 -= 1
        answer_day1 = (30 - day) + day1
    result = answer_year1 + answer_month1 + answer_day1
    print(result)
elif language.lower() == "pe" or language.lower() == "persian":
    print("سلام!")
    year = int(input("سال را وارد کنید: "))
    month = int(input("ماه را وارد کنید: "))
    day = int(input("روز را وارد کنید: "))
    year1 = int(input("سال فعلی را وارد کنید: "))
    month1 = int(input("ماه فعلی را وارد کنید: "))
    day1 = int(input("روز فعلی را وارد کنید: "))
    answer_year1 = (year1 - year) * 365
    answer_month1 = (month1 - month) * 30
    answer_day1 = day1 - day
    result = answer_year1 + answer_month1 + answer_day1
    if day > day1:
        answer_month1 -= 1
        answer_day1 = (30 - day) + day1
    result = answer_year1 + answer_month1 + answer_day1
    print(result)
else:
    print("invalid language, please restart program again")
    print("زبان وارد شده نادرست است. لطفاً برنامه را دوباره اجرا کنید")