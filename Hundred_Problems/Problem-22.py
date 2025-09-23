# create dictionary from tuples

def create_dictionary(list1: list[int], list2: list[str]) -> dict[int, str]:
    d = {}
    for i in range(len(list1)):
        d[list1[i]] = list2[i]
    return d

# def create_dictionary(list1: list[int], list2: list[str]) -> dict[int, str]:
#     d = zip(list1, list2) #zip() คือฟังก์ชันที่จับค่าจากหลายลิสต์มาตามตำแหน่งเดียวกัน แล้วรวมเป็นคู่ tuple ในแต่ละตำแหน่ง
#     return dict(d)

list1 = [1,2,3,4]
list2 = ["blue","green","pink","yellow"]
print(create_dictionary(list1, list2))