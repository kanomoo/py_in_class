# currency conversion between 5 currencies

# def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
#     from_currency = from_currency.upper()
#     to_currency = to_currency.upper()
#     con = {"EUR":0.85,"GBP":0.75,"JPY":110.0,"THB":32.0}
#
#     if from_currency == "USD":
#         for k,v in con.items():
#             if to_currency == k:
#                 return amount * v
#     else:
#         for name,coin in con.items():
#             if from_currency == name:
#                 usb = amount / coin
#             if to_currency == name:
#                 return round(usb * coin,2)

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    coin = {"USB":1,"EUR":0.85,"GBP":0.75,"JPY":110.0,"THB":32.0}
    if from_currency not in coin or to_currency not in coin:
        return "not supported"
    usb = amount / coin[from_currency] # 0.9 = 1000 / 110
    convert = usb * coin[to_currency]
    return round(convert,2)

amount = 1000.0
from_currency = "USB"
to_currency = "USB"
print(convert_currency(amount, from_currency, to_currency))