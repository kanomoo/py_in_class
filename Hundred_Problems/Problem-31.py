# county Sales Analysis

# def highest_sales_country(sales: dict[str, int]) -> tuple[str, int]:
#     max = 0
#     for i in sales:
#         if sales[i] > max:
#             max = sales[i]
#     for n in sales:
#         if sales[n] == max:
#             return n,max

def highest_sales_country(sales: dict[str, int]) -> tuple[str, int]:
    Max = max(sales, key=sales.get) #key=sales.get คือให้ใช้ยอดขาย (value) ของแต่ละประเทศในการเปรียบเทียบ
    return Max, sales[Max]

sales_data = {
    "Thailand": 1500,
    "Laos": 1200,
    "Vietnam": 1800,
    "Japan": 1700,
    "China": 2000
}
print(highest_sales_country(sales_data))