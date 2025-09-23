num = input("Input: ")
out = num.upper().split(" ")
mess = ""
for i in out:
    out1 = {"ONE":"1","TWO":"2","THREE":"3","FOUR":"4","FIVE":"5","SIX":"6","SEVEN":"7","EIGHT":"8","NIGHT":"9","TEN":"10"
            ,"HUNDRED":"00","THOUSAND":"000","MILLION":"000000"}
    for n in out1:
        if i == n:
            mess += (out1[i])
            break
print("Output:",format(int(mess),","))