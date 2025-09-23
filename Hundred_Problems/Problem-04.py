#average calculation
def calculate_sum_and_average() -> None:
    data = []
    for i in range(5):
        number = float(input(f"Enter number {i+1}: "))
        data.append(number)
    total = sum(data)
    average = total / len(data)
    print(f"\nSum : {total:.2f}\nAverage: {average:.2f}")

calculate_sum_and_average()