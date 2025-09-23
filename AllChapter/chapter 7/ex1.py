def find_max(num):
    Max = 0
    for i in str(num):
        if int(i) > int(Max): Max = i
    return Max

print(find_max(6378942))

# def find_max(num):return(max(str(num)))
#
# print(find_max(6378942))