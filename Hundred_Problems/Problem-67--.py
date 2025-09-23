# calculate age from date of birth

# from datetime import date
# from dateutil.relativedelta import relativedelta
#
# def calculate_age(day_of_birth: int, month_of_birth: int, year_of_birth: int) -> tuple[int, int, int]:
#     birth_date = date(year_of_birth, month_of_birth, day_of_birth)
#     today = date.today()
#     diff = relativedelta(today, birth_date)
#     return diff.years, diff.months, diff.days



from datetime import date
from typing import Tuple

def calculate_age(day_of_birth: int, month_of_birth: int, year_of_birth: int) -> Tuple[int, int, int]:
    today = date.today()
    birth_date = date(year_of_birth, month_of_birth, day_of_birth)

    # คำนวณปี เดือน วัน แบบ manual
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # ถ้าวันติดลบ ต้องยืมเดือนก่อนหน้า
    if days < 0:
        months -= 1
        # หาวันทั้งหมดในเดือนก่อนหน้า
        from calendar import monthrange
        prev_month = today.month - 1 if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1
        days += monthrange(prev_year, prev_month)[1]

    # ถ้าเดือนติดลบ ต้องยืมปี
    if months < 0:
        years -= 1
        months += 12

    return years, months, days


print(calculate_age(15,8,1990))