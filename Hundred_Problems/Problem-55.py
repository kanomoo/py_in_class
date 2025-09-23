# convert thai baht (thb) to multiple currencies

# def convert_thb_to_currency(amount: float, to_currency: str) -> float:
#     coin = {"USD":0.030,"EUR":0.027,"GBP":0.023,"JPY":3.4,"AUD":0.045}
#     for name,money in coin.items():
#         if to_currency.upper() == name:
#             return amount * money
#     return "Please check the target currency."

def convert_thb_to_currency(amount: float, to_currency: str) -> float:
    coin = {"USD":0.030,"EUR":0.027,"GBP":0.023,"JPY":3.4,"AUD":0.045}
    if to_currency.upper() not in coin:
        return "not support"
    return amount * coin[to_currency.upper()]

amount = 1000
to_currency = "JPy"
print(convert_thb_to_currency(amount, to_currency))