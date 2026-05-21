# convert buddhist Era(B.E.) to gregorian year (a.d.)

# def convert_be_to_ad(be_year: int) -> int:
#     return be_year - 543

# print(convert_be_to_ad(2567))

def convert_be_to_ad(be_year: int) -> int:
    return be_year - 543

if __name__ == "__main__":
    print(convert_be_to_ad(be_year = 2567))