# currency conversion class
class CurrencyConverter:

    def __init__(self,amount: float, currency: str):
        self.amount = amount
        self.currency = currency

    def convert_to(self, target_currency: str) -> float:
        self.target_currency = target_currency
        con_usb = {"USD": 1, "EUR": 0.85, "GBP": 0.75, "JPY": 110, "THB": 32}
        con_rate = {"USD": 1, "EUR": 1 / 0.85, "GBP": 1 / 0.75, "JPY": 1 / 110, "THB": 1 / 32}
        amount = self.amount * con_rate[self.currency.upper()]
        amount = amount * con_usb[self.target_currency.upper()]
        return amount

# amount = 100.0
# currency = "USD"
# target_currency = "EUR"
# money = CurrencyConverter(amount,currency)
# print(money.convert_to(target_currency))


amount = int(input("amount : "))
currency = input("currency : ")
target_currency = input("target : ")
money = CurrencyConverter(amount,currency)
money_con = money.convert_to(target_currency)
print(f"{amount} {currency} is equal to {money_con} {target_currency}")
