# calculate the number of days between two gregorian dates

# def days_between_dates(dat1: str, date2: str) -> int:
#     day1 = dat1.split("-")
#     day2 = date2.split("-")
#     return int(str(int(day1[2]) - int(day2[2])).strip("-"))

from datetime import datetime

# def days_between_dates(date1: str, date2: str) -> int:
#     d1 = datetime.strptime(date1, "%Y-%m-%d") #datetime.strptime() แปลง string ให้กลายเป็น datetime object
#     d2 = datetime.strptime(date2, "%Y-%m-%d")
#     return abs((d2 - d1).days) # abs() ทำให้แน่ใจว่าได้ค่าบวกเสมอไม่ว่าลำดับวันที่จะเป็นอย่างไร

def days_between_dates(date1: str, date2: str) -> int:
    d1 = datetime.strptime(date1,"%Y-%m-%d")
    d2 = datetime.strptime(date2,"%Y-%m-%d")
    return abs(d2 - d1).days

date1 = "2024-08-01"
date2 = "2024-08-10"
print(days_between_dates(date1, date2))