# นายนะจ็ะ
result = ""

head = "| Celsius  | Fahrenheit |  Kelvin |"
line = len(head) * "="
start = int(input("Enter start Celsius: "))
end = int(input("Enter end Celsius: "))
step = int(input("Enter step: "))
while step < 0:
    print("! Step must be > 0.\n")
    step = int(input("Enter step: "))

print(line,head,line,sep="\n")
if start > end:
    for c in range(end, start + 1, step):
        print(f"|  {c:>5.2f}   |   {c * 9 / 5 + 32:<9.2f}|  {c + 273.15:.2f} |")
else:
    for c in range(start,end+1,step):
        print(f"|  {c:>5.2f}   |   {c * 9/5 + 32:<9.2f}|  {c + 273.15:.2f} |")
print(line)