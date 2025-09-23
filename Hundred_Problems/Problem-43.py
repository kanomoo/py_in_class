# automatic coin exchange

# def calculate_coins(amount: int) -> tuple[int, int, int, int]:
#     if amount % 2 != 0:
#         return (amount // 10, amount % 10 // 5, amount % 5 // 2, amount % 5 // 2 )
#     else:
#         return (amount // 10, amount % 10 // 5, amount % 5 // 2, amount % 2 )

# def calculate_coins(amount: int) -> tuple[int, int, int, int]:
#     c10 = amount // 10       # คำนวณจำนวนเหรียญ 10 ที่ใช้ได้จากจำนวนเงิน
#     amount %= 10             # หารเอาเศษเหลือจากการใช้เหรียญ 10 ออก
#     c5 = amount // 5         # คำนวณจำนวนเหรียญ 5 ที่ใช้ได้จากยอดที่เหลือ
#     amount %= 5              # หารเอาเศษเหลือจากการใช้เหรียญ 5 ออก
#     c2 = amount // 2         # คำนวณจำนวนเหรียญ 2 ที่ใช้ได้จากยอดที่เหลือ
#     amount %= 2              # หารเอาเศษเหลือจากการใช้เหรียญ 2 ออก
#     c1 = amount              # เหรียญ 1 คือค่าที่เหลือสุดท้าย
#     return c10, c5, c2, c1   # คืนค่าเป็น tuple (เหรียญ10, 5, 2, 1)


def calculate_coins(amount: int) -> tuple[int, int, int, int]:
    c10 = amount // 10
    amount %= 10
    c5 = amount // 5
    amount %= 5
    c2 = amount // 2
    amount %= 2
    c1 = amount
    return c10, c5, c2, c1

print(calculate_coins(28))