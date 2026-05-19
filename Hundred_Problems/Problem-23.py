# create dictionary from tuples

# def create_dictionary(tuple1: tuple[int, ...], tuple2: tuple[str, ...]) -> dict[int,str]:
#     d = dict(zip(tuple1,tuple2))
#     return d

# tuple1 = (1, 2, 3, 4)
# tuple2 = ("ant", "cat", "dog", "cow")
# print(create_dictionary(tuple1,tuple2))



# def create_dictionary(tuple1: tuple[int, ...], tuple2: tuple[str, ...]) -> dict[int, str]:
#     return {tuple1[i]: tuple2[i] for i in range(len(tuple1))}

def create_dictionary(tuple1: tuple[int, ...], tuple2: tuple[str, ...]) -> dict[int, str]:
    return dict(zip(tuple1, tuple2))

if __name__ == "__main__":
    tuple1 = (1, 2, 3, 4)
    tuple2 = ("ant", "cat", "dog", "cow")
    print(create_dictionary(tuple1, tuple2))
