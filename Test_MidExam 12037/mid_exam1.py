# นายปภาวิน ธิติชุณหกุล 6806021612037 it sec.c
start,result = int(input("Enter start Celsius: ")), ""
end = int(input("Enter end Celsius: "))
step = int(input("Enter steop: "))
while step <= 0:
    print("! Step must be > 0.\n")
    step = int(input("Enter step: "))
head = "| Celsius  | Fahrenheit |  Kelvin |"
line = len(head) * "="
if start > end :
    for i in range(end,start+1,step):
        result += f"|  {i:5.2f}   |   {(i * 9/5) +32:<9.2f}|  {(i + 273.15):6.2f} |\n"
else: 
    for i in range(start,end+1,step):
        result += f"|  {i:5.2f}   |   {(i * 9/5) +32:<9.2f}|  {(i + 273.15):6.2f} |\n"
print(line,head,line,result+line,sep="\n")