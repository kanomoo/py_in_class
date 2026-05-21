# # calculate the area of a rectangle
# def calculate_rectangle_area(width: float, length: float) -> float:
#     return float(width * length)

# print(calculate_rectangle_area(5,10))

def calculate_rectangle_area(width: float, length: float) -> float:
    return float(width * length)

if __name__ == "__main__":
    width, length = 5, 10
    print(calculate_rectangle_area(width, length))