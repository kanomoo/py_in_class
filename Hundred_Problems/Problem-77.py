# # currency conversion class
# class CurrencyConverter:

#     def __init__(self,amount: float, currency: str):
#         self.amount = amount
#         self.currency = currency

#     def convert_to(self, target_currency: str) -> float:
#         self.target_currency = target_currency
#         con_usb = {"USD": 1, "EUR": 0.85, "GBP": 0.75, "JPY": 110, "THB": 32}
#         con_rate = {"USD": 1, "EUR": 1 / 0.85, "GBP": 1 / 0.75, "JPY": 1 / 110, "THB": 1 / 32}
#         amount = self.amount * con_rate[self.currency.upper()]
#         amount = amount * con_usb[self.target_currency.upper()]
#         return amount

# # amount = 100.0
# # currency = "USD"
# # target_currency = "EUR"
# # money = CurrencyConverter(amount,currency)
# # print(money.convert_to(target_currency))


# amount = int(input("amount : "))
# currency = input("currency : ")
# target_currency = input("target : ")
# money = CurrencyConverter(amount,currency)
# money_con = money.convert_to(target_currency)
# print(f"{amount} {currency} is equal to {money_con} {target_currency}")


class CurrencyConverter:
    def __init__(self, amount: float, currency: str):
        self.amount, self.currency = amount, currency
    
    def convert_to(self, target_currency: str) -> float:
        currency = {"USD": 1, "EUR": 0.85, "GBP": 0.75, "JPY": 110, "THB": 32}
        return float(self.amount * currency[target_currency] / currency[self.currency])

if __name__ == "__main__":
    while True:
        select = input("1. Enter amount CurrencyConverter\n2. Display currency converter\n3. Exit program.\nSelect: "); print()
        match select:
            case "1":
                currency_con = CurrencyConverter(float(input("Enter amount: ")), input("Enter currency: ").upper()); print()
            case "2":
                target_currency = input("Enter target_currency: ").upper(); print()
                print(f"{currency_con.amount} {currency_con.currency} is equal to {currency_con.convert_to(target_currency)}\n")
            case "3": print("Exit program.", end = ""); exit()
            case _: print("No choice")

